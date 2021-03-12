var reminders = [];

function updateReminders() {
    console.log("update reminders")

    const data = {};
    data["morning_reminder"] = "08:00";
    data["shopping_reminder"] = "12:00";
    data["cooking_reminder"] = "18:00";
    data["evening_reminder"] = "22:00";
    $.ajax(
        {
            type: "POST",
            url: "http://localhost:8000/coordinator/reminder/",
            data: data,
            success: function (result) {
                //console.log(data)
                console.log(result)
                reminders = result.reminders
            },
            dataType: "json"
        }
    );
}

$(document).ready(function () {
        
    var proactiveIntervalId = setInterval(function() {
        console.log("check reminders")
        console.log(reminders)
        if(reminders.length > 0) {
            let now = new Date()
            let reminder = new Date()
            reminder.setHours(reminders[0].hour)
            reminder.setMinutes(reminders[0].minute)
            
            if(reminder <= now){
                const data = {};
                data["text"] = reminders[0].usecase;
                data["context"] = null;
                data["follow_up"] = null;
                data["preferences"] = JSON.parse(getCookie("userName"));
                $.ajax(
                    {
                        type: "POST",
                        url: "http://localhost:8000/coordinator/",
                        data: data,
                        success: function (result) {
                            //console.log(data)
                            //console.log(result)
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
        } else {
            //clearInterval(proactiveIntervalId);
            //console.log("currently no more reminders")
        }
        
    }, 100000);

    updateReminders();

    var updateIntervalId = setInterval(function() {
        
        updateReminders();
        
    }, 120000);
});