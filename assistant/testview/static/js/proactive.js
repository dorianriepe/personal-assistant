var reminders = [
    {"hour": 15, "minute": 10, "usecase": "hungry"},
    {"hour": 15, "minute": 15, "usecase": "next meeting"},
];

$(document).ready(function () {
        
    var intervalId = setInterval(function() {
        
        if(reminders.length > 0) {
            let now = new Date()
            let reminder = new Date()
            reminder.setHours(reminders[0].hour)
            reminder.setMinutes(reminders[0].minute)
            
            if(reminder <= now){
                //console.log(reminders[0].usecase)
                const data = {};
                data["text"] = reminders[0].usecase;
                data["context"] = null;
                data["follow_up"] = null;
                $.ajax(
                    {
                        type: "POST",
                        url: "http://localhost:8000/coordinator/",
                        data: data,
                        success: function (result) {
                            console.log(data)
                            console.log(result)
                            context = result.context;
                            follow_up = result.follow_up;
                            $("#dialog").append("<div class=\"assistant\"></div>");
                            $(".assistant").last().html(result.html);
                            speak(result.text)
                        },
                        dataType: "json"
                    }
                );


                reminders.shift();
            }
        }else {
            clearInterval(intervalId);
            console.log("currently no more reminders")
        }
        
    }, 5000);
});