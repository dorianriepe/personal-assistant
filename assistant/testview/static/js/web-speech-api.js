var messages = {
    "start": {
        msg: 'Click on the microphone icon and begin speaking.',
        class: 'alert-success'
    },
    "speak_now": {
        msg: 'Speak now.',
        class: 'alert-success'
    },
    "no_speech": {
        msg: 'No speech was detected. You may need to adjust your <a href="//support.google.com/chrome/answer/2693767" target="_blank">microphone settings</a>.',
        class: 'alert-danger'
    },
    "no_microphone": {
        msg: 'No microphone was found. Ensure that a microphone is installed and that <a href="//support.google.com/chrome/answer/2693767" target="_blank">microphone settings</a> are configured correctly.',
        class: 'alert-danger'
    },
    "allow": {
        msg: 'Click the "Allow" button above to enable your microphone.',
        class: 'alert-warning'
    },
    "denied": {
        msg: 'Permission to use microphone was denied.',
        class: 'alert-danger'
    },
    "blocked": {
        msg: 'Permission to use microphone is blocked. To change, go to chrome://settings/content/microphone',
        class: 'alert-danger'
    },
    "upgrade": {
        msg: 'Web Speech API is not supported by this browser. It is only supported by <a href="//www.google.com/chrome">Chrome</a> version 25 or later on desktop and Android mobile.',
        class: 'alert-danger'
    },
    "stop": {
        msg: 'Stop listening, click on the microphone icon to restart',
        class: 'alert-success'
    },
    "copy": {
        msg: 'Content copy to clipboard successfully.',
        class: 'alert-success'
    },
}

var final_transcript = '';
var recognizing = false;
var ignore_onend;
var start_timestamp;
var recognition;

var context = null;

var follow_up = null;

$(document).ready(function () {
    if (!('webkitSpeechRecognition' in window)) {
        upgrade();
    } else {
        showInfo('start');
        start_button.style.display = 'inline-block';
        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onstart = function () {
            recognizing = true;
            showInfo('speak_now');
            start_img.src = 'static/images/mic-animation.gif';
        };

        recognition.onerror = function (event) {
            if (event.error === 'no-speech') {
                start_img.src = 'static/images/mic.gif';
                showInfo('no_speech');
                ignore_onend = true;
            }
            if (event.error === 'audio-capture') {
                start_img.src = 'static/images/mic.gif';
                showInfo('no_microphone');
                ignore_onend = true;
            }
            if (event.error === 'not-allowed') {
                if (event.timeStamp - start_timestamp < 100) {
                    showInfo('blocked');
                } else {
                    showInfo('denied');
                }
                ignore_onend = true;
            }
        };

        recognition.onend = function () {
            recognizing = false;
            if (ignore_onend) {
                return;
            }
            start_img.src = 'static/images/mic.gif';
            if (!final_transcript) {
                showInfo('start');
                return;
            }
            showInfo('stop');
            if (window.getSelection) {
                window.getSelection().removeAllRanges();
                var range = document.createRange();
                range.selectNode(document.getElementById('final_span'));
                window.getSelection().addRange(range);
            }
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
            final_transcript = capitalize(final_transcript);
            final_span.innerHTML = linebreak(final_transcript);
            interim_span.innerHTML = linebreak(interim_transcript);
        };
    }
});


function upgrade() {
    start_button.style.visibility = 'hidden';
    showInfo('upgrade');
}


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

$("#ajax_button").click(function () {
    const data = {};
    data["text"] = document.getElementById('final_span').innerText;
    data["context"] = context;
    data["follow_up"] = follow_up;
    data["preferences"] = JSON.parse(getCookie("userName"));
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
                console.log(data)
                $("#div1").html(result.html);
                context = result.context;
                follow_up = result.follow_up;
                speak(result.text)
                console.log(context);
            },
            dataType: "json"
        }
    );
});

setTimeout(function () {
    context = null;
    follow_up = null
}, 1000);


const synth = window.speechSynthesis;


function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    const voices = speechSynthesis.getVoices();
    utterance.voice = voices[41]
    utterance.lang = "en-US"
    utterance.pitch = 1;
    utterance.rate = 1;
    synth.speak(utterance);
}


$("#start_button").click(function () {
    if (recognizing) {
        recognition.stop();
        return;
    }
    final_transcript = '';
    recognition.lang = 'en-US';
    recognition.start();
    ignore_onend = false;
    final_span.innerHTML = '';
    interim_span.innerHTML = '';
    start_img.src = 'static/images/mic-slash.gif';
    showInfo('allow');
    start_timestamp = event.timeStamp;
});


function showInfo(s) {
    if (s) {
        var message = messages[s];
        $("#info").html(message.msg);
        $("#info").removeClass();
        $("#info").addClass('alert');
        $("#info").addClass(message.class);
    } else {
        $("#info").removeClass();
        $("#info").addClass('d-none');
    }
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
    if (form[0].usrname.value == "" || form[0].lcation.value == "" || form[0].bndesliga.value == "" || form[0].clb.value == "" || form[0].nws.value == "") {
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
    // console.log();
    setCookie("userName", JSON.stringify(obj));
    closeNav();
    return true;
}


function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
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
        document.getElementById("div1").innerHTML = "How can I help you? " + data.name;
        document.getElementsByTagName('form')[0].usrname.value = data.name;
        document.getElementsByTagName('form')[0].bndesliga.value = data.liga;
        document.getElementsByTagName('form')[0].clb.value = data.club;
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
    } else {
        openNav()
    }
}

function clubs(form) {
    var clubs1 = [];
    clubs1[0] = 'Bayern München';
    clubs1[1] = 'Borussia Dortmund';
    clubs1[2] = 'FC Schalke 04';
    clubs1[3] = '1.FC Köln';
    clubs1[4] = 'Borussia Mönchengladbach';
    clubs1[5] = 'Eintracht Frankfurt';
    clubs1[6] = 'Vfb Stuttgart';
    clubs1[7] = 'Weder Bremen';
    clubs1[8] = '1.FC Union Berlin';
    clubs1[9] = 'Herta BSC';
    clubs1[10] = 'Bayer 04 Leverkusen';
    clubs1[11] = 'SC Freiburg';
    clubs1[12] = 'Vfl Wolfsburg';
    clubs1[13] = 'FC Augsburg';
    clubs1[14] = 'Arminia Bielefeld';
    clubs1[15] = '1.FSV Mainz 05';
    clubs1[16] = 'TSG 1899 Hoffenheim';
    clubs1[17] = 'RB Leipzig';


    var clubs2 = [];
    clubs2[0] = 'VFL Bochum';
    clubs2[1] = 'Hamburger SV';
    clubs2[2] = 'Holstein Kiel';
    clubs2[3] = 'SVgg Greuther Fürth';
    clubs2[4] = 'Karlsruher SC';
    clubs2[5] = '1.FC Heidenheim';
    clubs2[6] = 'Fortuna Düsseldorf';
    clubs2[7] = 'Hannorver 96';
    clubs2[8] = 'Erzgebirge Aue';
    clubs2[9] = 'FC St. Pauli';
    clubs2[10] = 'SC Paderborn 07';
    clubs2[11] = 'Jahn Regensburg';
    clubs2[12] = 'SV Darmstadt 98';
    clubs2[13] = '1.FC Nürnberg';
    clubs2[14] = 'Eintracht Braunschweig';
    clubs2[15] = 'Vfl Osnabrück';
    clubs2[16] = 'SV Sandhausen';
    clubs2[17] = 'Würzurger Kickers';
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



