class HTMLResponseBuilder:
    
    use_case = ""

    def __init__(self):
        self.use_case = ""

    '''
    text: String, example: "Here are the next departures:"
    departures: [
        {   
            "time": "14:07", 
            "train": "S1 Herrenberg", 
            "plate": "Plate 1" 
        },...
    ]
    '''
    def bahn(self, text, departures):
        html = "<p>"+text+"</p>"
        for departure in departures:
            html += "<div class=\"list-time-title\"><div class=\"time\">"+departure["time"]+"</div><div class=\"train\">"+departure["train"]+"</div><div class=\"plate\">"+departure["plate"]+"</div></div>"
        return html