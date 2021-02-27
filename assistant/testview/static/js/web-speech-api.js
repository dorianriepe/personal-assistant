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

var two_line = /\n\n/g;
var one_line = /\n/g;

function linebreak(s) {
    return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
}

var first_char = /\S/;

function capitalize(s) {
    return s.replace(first_char, function (m) {
        return m.toUpperCase();
    });
}
$("#ajax_button").click(function () {
    const data = {};
    data["text"] = document.getElementById('final_span').innerText;
    $.ajax(
        {
            type: "POST",
            url: "http://localhost:8000/coordinator/",
            data: data,
            success: function (result) {
                console.log(result)
                $("#div1").html(result.html);
                speak(result.text)
            },
            dataType: "json"
        }
    );
});

const synth = window.speechSynthesis;


function speak(text){
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
    start_img.src = 'images/mic-slash.gif';
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
