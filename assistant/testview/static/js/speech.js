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