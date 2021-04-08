var final_transcript = '';
var recognizing = false;
var ignore_onend;
var start_timestamp;
var recognition;

var text = "";

var context = null;
var follow_up = null;

const synth = window.speechSynthesis;

$(document).ready(function () {


    $("#start").click(function () {
        if (recognizing) {
            recognition.stop();
            return;
        }
        final_transcript = '';
        recognition.lang = 'en-US';
        recognition.start();
        ignore_onend = false;
        start_timestamp = event.timeStamp;
    });


    if (!('webkitSpeechRecognition' in window)) {
        console.log("WebKitSpeechAPI not supported")
    } else {
        console.log("WebKitSpeechAPI is supported")

        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onstart = function () {
            recognizing = true;
            text = "";
        };

        recognition.onerror = function (event) {
            console.log("onerror")
            if (event.error === 'no-speech') {
                console.log("no speech")
                ignore_onend = true;
            }
            if (event.error === 'audio-capture') {
                console.log("no microphone")
                ignore_onend = true;
            }
            if (event.error === 'not-allowed') {
                if (event.timeStamp - start_timestamp < 100) {
                    console.log("blocked")
                } else {
                    console.log("denied")
                }
                ignore_onend = true;
            }
        };

        recognition.onend = function (event) {
            recognizing = false;
            if (ignore_onend) {
                return;
            }
            if (!final_transcript) {
                return;
            }
            console.log(text);
            $("#dialog").append("<div class=\"user\"></div>");
            $(".user").last().text(text);

            const data = {};
            data["text"] = text;
            data["context"] = context;
            data["follow_up"] = follow_up;
            data["preferences"] = getCookie("userName");
            if (data["preferences"] == "") {
                openNav();
                return;
            }
            setTimeout(function () {
                context = null;
                follow_up = null
            }, 100000);

            $.ajax(
                {
                    type: "POST",
                    url: "http://localhost:8000/coordinator/",
                    data: data,
                    success: function (result) {
                        console.log(data);
                        console.log(result);
                        context = result.context;
                        follow_up = result.follow_up;
                        if (result.text != null) {
                            $("#dialog").append("<div class=\"assistant\"></div><br><br>");
                            $(".assistant").last().html(result.html);
                            document.body.scrollTop = document.body.scrollHeight;
                            document.documentElement.scrollTop = document.body.scrollHeight;
                            speak(result.text)

                        }

                    },
                    dataType: "json"
                }
            );
        };

        recognition.onresult = function (event) {
            var interim_transcript = '';
            for (var i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                    final_transcript += event.results[i][0].transcript;
                } else {
                    interim_transcript += event.results[i][0].transcript;
                }
            }
            final_transcript = linebreak(capitalize(final_transcript));
            text += final_transcript;
        };

    }

});

function linebreak(s) {
    var one_line = /\n/g;
    var two_line = /\n\n/g;
    return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
}

function capitalize(s) {
    var first_char = /\S/;
    return s.replace(first_char, function (m) {
        return m.toUpperCase();
    });
}


function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    const voices = speechSynthesis.getVoices();
    utterance.voice = voices[41]
    utterance.lang = "en-US"
    utterance.pitch = 1;
    utterance.rate = 1;
    synth.speak(utterance);
}


function openNav() {
    document.getElementById("myNav").style.display = "block";
}

function closeNav() {
    checkCookie();
    document.getElementById("myNav").style.display = "none";
}

var today = new Date();
var expiry = new Date(today.getTime() + 30 * 24 * 3600 * 1000); // plus 30 days

function setCookie(name, value) {
    document.cookie = name + "=" + escape(value) + "; path=/; expires=" + expiry.toGMTString();
}

function putCookie(form)
//this should set the UserName cookie to the proper value;
{
    var obj = {};
    if (form[0].usrname.value == "" || form[0].lcation.value == "" || form[0].bndesliga.value == "" || form[0].clb.value == "" || form[0].nws.value == "" || form[0].dts.value == "" || form[0].hlth.value == "" || form[0].sttion.value == "") {
        alert("please fill all fields");
        return false;
    }
    switch (form[0].nws.value) {
        case "New York Times":
            obj["news"] = "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml";
            break;
        case "The Economist":
            obj["news"] = "https://www.economist.com/the-world-this-week/rss.xml";
            break;
        case "Deutsche Welle":
            obj["news"] = "https://rss.dw.com/rdf/rss-en-ger";

    }

    obj["name"] = form[0].usrname.value;
    obj["location"] = form[0].lcation.value
    obj["liga"] = form[0].bndesliga.value;
    obj["club"] = form[0].clb.value;
    obj["diet"] = form[0].dts.value;
    obj["health"] = form[0].hlth.value;
    obj["station"] = form[0].sttion.value;

    // console.log();
    setCookie("userName", JSON.stringify(obj));
    closeNav();
    return true;
}


function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(unescape(document.cookie));
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}


function checkCookie() {
    var user = getCookie("userName");
    if (user != "") {
        data = JSON.parse(user);
        document.getElementsByTagName('form')[0].usrname.value = data.name;
        document.getElementsByTagName('form')[0].bndesliga.value = data.liga;
        document.getElementsByTagName('form')[0].lcation.value = data.location;
        document.getElementsByTagName('form')[0].clb.value = data.club;
        document.getElementsByTagName('form')[0].dts.value = data.diet;
        document.getElementsByTagName('form')[0].hlth.value = data.health;
        document.getElementsByTagName('form')[0].nws.value = data.news;
        document.getElementsByTagName('form')[0].sttion.value = data.station;
        switch (data.news) {
            case "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml":
                document.getElementsByTagName('form')[0].nws.value = "News York Times";
                break;
            case "https://www.economist.com/the-world-this-week/rss.xml":
                document.getElementsByTagName('form')[0].nws.value = "The Economist";
                break;
            case "https://rss.dw.com/rdf/rss-en-ger":
                document.getElementsByTagName('form')[0].nws.value = "Deutsche Welle";
        }
        clubs(document.getElementsByName('bndesliga'));
        resetList(document.getElementsByName('nws'));
        resetList(document.getElementsByName('dts'));
        resetList(document.getElementsByName('hlth'));
    } else {
        openNav()
    }
}

function clubs(form) {
    var clubs1 = [];
    clubs1[0] = 'Bayern';
    clubs1[1] = 'Dortmund';
    clubs1[2] = 'Schalke';
    clubs1[3] = 'Köln';
    clubs1[4] = 'Gladbach';
    clubs1[5] = 'Frankfurt';
    clubs1[6] = 'Stuttgart';
    clubs1[7] = 'Bremen';
    clubs1[8] = 'Union Berlin';
    clubs1[9] = 'Herta';
    clubs1[10] = 'Leverkusen';
    clubs1[11] = 'Freiburg';
    clubs1[12] = 'Wolfsburg';
    clubs1[13] = 'Augsburg';
    clubs1[14] = 'Bielefeld';
    clubs1[15] = 'Mainz';
    clubs1[16] = 'Hoffenheim';
    clubs1[17] = 'Leipzig';


    var clubs2 = [];
    clubs2[0] = 'Bochum';
    clubs2[1] = 'Hamburg';
    clubs2[2] = 'Kiel';
    clubs2[3] = 'SVgg Greuther Fürth';
    clubs2[4] = 'Karlsruhe';
    clubs2[5] = 'Heidenheim';
    clubs2[6] = 'Düsseldorf';
    clubs2[7] = 'Hannorver';
    clubs2[8] = 'Erzgebirge Aue';
    clubs2[9] = 'St. Pauli';
    clubs2[10] = 'Paderborn';
    clubs2[11] = 'Regensburg';
    clubs2[12] = 'Darmstadt';
    clubs2[13] = 'Nürnberg';
    clubs2[14] = 'Braunschweig';
    clubs2[15] = 'Osnabrück';
    clubs2[16] = 'Sandhausen';
    clubs2[17] = 'Würzurger';
    var options = '';

    form[0].addEventListener('click', () => {
        if (form[0].value) {
            form[0].value = "";
            document.getElementsByTagName('form')[0].clb.value = "";
            resetList(document.getElementsByName('clb'));

        }
    });

    if (form[0].value == "1.Bundesliga") {
        for (var i = 0; i < clubs1.length; i++) {
            options += '<option value="' + clubs1[i] + '" />';
        }
    } else {
        for (var i = 0; i < clubs2.length; i++) {
            options += '<option value="' + clubs2[i] + '" />';
        }
    }
    document.getElementById('club').innerHTML = options;

}

function resetList(form) {
    form[0].addEventListener('click', () => {
        if (form[0].value) {
            form[0].value = "";
        }
    });
}



