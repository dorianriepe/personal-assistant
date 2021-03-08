class HTMLResponseBuilder:
    
    use_case = ""

    def __init__(self):
        self.use_case = ""

    def img_title_subtitle(self, text, title, subtitle, image_url, link):
        
        html = "<p>"+text+"</p>"
        html += "<div class=\"img-title-subtitle\">"
        html += "<div class=\"image\"><img src=\""+image_url+"\" alt=\"Playlist Artwork\"></div>"
        html += "<div class=\"title\"><a class=\"title\" href=\""+link+"\">"+title+"</a></div>"
        html += "<div class=\"subtitle\"><a>"+subtitle+"</a></div>"
        html += "</div>"

        return html

    def time_title_subtitle(self, text, title, subtitle, from_time, to_time, link):
        
        html = "<p>"+text+"</p>"
        html += "<div class=\"time-title-subtitle\">"
        html += "<div class=\"time\"><a>"+from_time+"<br>"+to_time+"</a></div>"
        html += "<div class=\"title\"><a class=\"title\" href=\""+link+"\">"+title+"</a></div>"
        html += "<div class=\"subtitle\"><a>"+subtitle+"</a></div>"
        html += "</div>"

        return html

    def list_time_title(self, text, departures):
        html = "<p>"+text+"</p>"
        for departure in departures:
            html += "<div class=\"list-time-title\"><div class=\"time\">"+departure["time"]+"</div><div class=\"train\">"+departure["train"]+"</div><div class=\"plate\"></div></div>"
        return html

    def rank_image_name(self, text, table):
        html = "<p>"+text+"</p>"
        for rank in table:
            html += "<div class=\"rank-image-name\">"
            html += "<div class=\"place\"><a>"+str(rank["rank"])+"</a></div>"
            html += "<div class=\"image\"><img src=\""+rank["teamIconUrl"]+"\" alt=\"Vereins Logo\"></div>"
            html += "<div class=\"name\">"+rank["clubShortName"]+"</div>"
            html += "</div>"
        return html