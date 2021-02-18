from unittest import TestCase
from unittest.mock import patch

from news_wrapper import NewsScraper


class TestNewsScraper(TestCase):

    @patch('news_wrapper.NewsScraper._getResponse')
    def test_get_article_list1(self, mock__getResponse):
        inst = NewsScraper.getInstance('http://127.0.0.1')
        ml = b'<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n<rss version="2.0" ' \
             b'xmlns:content="http://purl.org/rss/1.0/modules/content/">\n  <channel>\n    <title>tagesschau.de - Die ' \
             b'Nachrichten der ARD</title>\n    <link>https://www.tagesschau.de</link>\n    ' \
             b'<description>tagesschau.de</description>\n    <language>de</language>\n    <copyright>ARD-aktuell / ' \
             b'tagesschau.de</copyright>\n    <lastBuildDate>Thu, 18 Feb 2021 22:18:19 +0100</lastBuildDate>\n    ' \
             b'<docs>http://blogs.law.harvard.edu/tech/rss</docs>\n    <ttl>10</ttl>\n    <item>\n      ' \
             b'<title>NASA-Rover "Perseverance" gelingt Mars-Landung</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/mars-landung-101.html</link>\n      <pubDate>Thu, 18 Feb 2021 ' \
             b'21:56:21 +0100</pubDate>\n      <description>Der NASA-Rover "Perseverance" ist nach sechs Monaten ' \
             b'Flugzeit erfolgreich auf dem Mars gelandet. Er soll mehrere Jahre lang nach Spuren fr\xc3\xbcheren ' \
             b'mikrobiellen Lebens suchen. Au\xc3\x9ferdem wird er das Klima und die Geologie des Planeten ' \
             b'erforschen.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/mars-landung-101.html</guid>\n      <content:encoded><![CDATA[' \
             b'\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/mars-landung-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/sendungsbild-702687~_v-mittel16x9.jpg" ' \
             b'alt="Sendungsbild" /></a>\n                <br/>\n                <br/>\n            \n            Der ' \
             b'NASA-Rover &quot;Perseverance&quot; ist nach sechs Monaten Flugzeit erfolgreich auf dem Mars gelandet. ' \
             b'Er soll mehrere Jahre lang nach Spuren fr\xc3\xbcheren mikrobiellen Lebens suchen. Au\xc3\x9ferdem ' \
             b'wird er das Klima und die Geologie des Planeten erforschen. <a ' \
             b'href="https://www.tagesschau.de/ausland/mars-landung-101.html">mehr</a>\n        </p>\n        <ul>\n  ' \
             b'              \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/mars-landung-101.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>PEI bewertet ' \
             b'AstraZeneca-Vakzin weiter positiv</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/impfen-debatte-105.html</link>\n      <pubDate>Thu, 18 Feb 2021 ' \
             b'21:45:03 +0100</pubDate>\n      <description>Impfreaktionen, Krankschreibungen und geplatzte ' \
             b'Impftermine - das AstraZeneca-Vakzin hat f\xc3\xbcr Diskussionen gesorgt. Das Paul-Ehrlich-Institut ' \
             b'h\xc3\xa4lt den Impfstoff weiter f\xc3\xbcr wirksam und sicher. \xc3\x84rzte und Politiker versuchen ' \
             b'Vertrauen zu schaffen.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/inland/impfen-debatte-105.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/inland/impfen-debatte-105.html"><img ' \
             b'src="https://www.tagesschau.de/inland/astrazeneca-127~_v-mittel16x9.jpg" alt="Spritze mit dem ' \
             b'AstraZeneca Covid-19-Impfstoff| Bildquelle: AFP" /></a>\n                <br/>\n                ' \
             b'<br/>\n            \n            Impfreaktionen, Krankschreibungen und geplatzte Impftermine - das ' \
             b'AstraZeneca-Vakzin hat f\xc3\xbcr Diskussionen gesorgt. Das Paul-Ehrlich-Institut h\xc3\xa4lt den ' \
             b'Impfstoff weiter f\xc3\xbcr wirksam und sicher. \xc3\x84rzte und Politiker versuchen Vertrauen zu ' \
             b'schaffen. <a href="https://www.tagesschau.de/inland/impfen-debatte-105.html">mehr</a>\n        </p>\n  ' \
             b'      <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/inland/impfen-debatte-105.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>Livestream: Die ' \
             b'Marslandung von "Perserverance"</title>\n      ' \
             b'<link>https://www.tagesschau.de/multimedia/livestream-1-107.html</link>\n      <pubDate>Thu, ' \
             b'18 Feb 2021 21:42:57 +0100</pubDate>\n      <description>Nach rund sechs Monaten Flugzeit landet der ' \
             b'US-Rover "Perseverance" auf dem Mars landen. Sehen Sie das Landeman\xc3\xb6ver und die ersten Bilder ' \
             b'vom roten Planeten hier live.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/multimedia/livestream-1-107.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/multimedia/livestream-1-107.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/mars-preseverance-103~_v-mittel16x9.jpg" alt="Landung ' \
             b'der Mars-Sonde &quot;Preseverance&quot; | Bildquelle: picture alliance/dpa/NASA" /></a>\n              ' \
             b'  <br/>\n                <br/>\n            \n            Nach rund sechs Monaten Flugzeit landet der ' \
             b'US-Rover &quot;Perseverance&quot; auf dem Mars landen. Sehen Sie das Landeman\xc3\xb6ver und die ' \
             b'ersten Bilder vom roten Planeten hier live. <a ' \
             b'href="https://www.tagesschau.de/multimedia/livestream-1-107.html">mehr</a>\n        </p>\n        ' \
             b'<ul>\n                \n            </ul>\n        </p>\n        \n    ]]></content:encoded>\n    ' \
             b'</item>\n    <item>\n      <title>Leverkusen verliert nach furioser Aufholjagd gegen Bern</title>\n    ' \
             b'  <link>https://www.tagesschau.de/regional/nordrheinwestfalen/europa-league-leverkusen-bern-101.html' \
             b'</link>\n      <pubDate>Thu, 18 Feb 2021 21:15:45 +0100</pubDate>\n      <description>Nach einer ' \
             b'extrem schwachen ersten Halbzeit glich Leverkusen im Europa League-Spiel gegen Bern einen 0:3 ' \
             b'R\xc3\xbcckstand aus. Doch ein sp\xc3\xa4ter Treffer der Schweizer machte die Aufholjagd ' \
             b'zunichte.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/regional/nordrheinwestfalen/europa-league-leverkusen-bern-101.html' \
             b'</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/regional/nordrheinwestfalen/europa-league-leverkusen-bern-101.html' \
             b'"><img src="https://www.tagesschau.de/regional/nordrheinwestfalen/wdr-image-77155~_v-mittel16x9.jpg" ' \
             b'alt="Young Boys Bern kurz vor dem 2:0| Bildquelle: imago images/Just Pictures" /></a>\n                ' \
             b'<br/>\n                <br/>\n            \n            Nach einer extrem schwachen ersten Halbzeit ' \
             b'glich Leverkusen im Europa League-Spiel gegen Bern einen 0:3 R\xc3\xbcckstand aus. Doch ein ' \
             b'sp\xc3\xa4ter Treffer der Schweizer machte die Aufholjagd zunichte. <a ' \
             b'href="https://www.tagesschau.de/regional/nordrheinwestfalen/europa-league-leverkusen-bern-101.html' \
             b'">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        ' \
             b'<p><a href="https://www.tagesschau.de/regional/nordrheinwestfalen/europa-league-leverkusen-bern-101' \
             b'.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    ' \
             b'<item>\n      <title>Proteste in Myanmar: Hackerangriffe und Stra\xc3\x9fenblockaden</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/asien/myanmar-proteste-hackerangriffe-autoblockaden-101.html' \
             b'</link>\n      <pubDate>Thu, 18 Feb 2021 20:47:11 +0100</pubDate>\n      <description>Die Proteste in ' \
             b'Myanmar gegen die Milit\xc3\xa4rjunta nehmen neue Formen an: Autos und Motorr\xc3\xa4der blockieren ' \
             b'die Stra\xc3\x9fen, Hacker greifen Webseiten der Armee an. Auch der internationale Druck auf das ' \
             b'Milit\xc3\xa4r steigt.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/asien/myanmar-proteste-hackerangriffe-autoblockaden-101.html' \
             b'</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/asien/myanmar-proteste-hackerangriffe-autoblockaden-101.html' \
             b'"><img src="https://www.tagesschau.de/multimedia/bilder/myanmar-blockade-101~_v-mittel16x9.jpg" ' \
             b'alt="Demonstrierende auf Motorr\xc3\xa4dern blockieren in Rangun eine Stra\xc3\x9fe und zeigen den ' \
             b'Drei-Finger-Gru\xc3\x9f.| Bildquelle: AP" /></a>\n                <br/>\n                <br/>\n       ' \
             b'     \n            Die Proteste in Myanmar gegen die Milit\xc3\xa4rjunta nehmen neue Formen an: Autos ' \
             b'und Motorr\xc3\xa4der blockieren die Stra\xc3\x9fen, Hacker greifen Webseiten der Armee an. Auch der ' \
             b'internationale Druck auf das Milit\xc3\xa4r steigt. <a ' \
             b'href="https://www.tagesschau.de/ausland/asien/myanmar-proteste-hackerangriffe-autoblockaden-101.html' \
             b'">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        ' \
             b'<p><a href="https://www.tagesschau.de/ausland/asien/myanmar-proteste-hackerangriffe-autoblockaden-101' \
             b'.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    ' \
             b'<item>\n      <title>Nach Explosion in Lidl-Zentrale: Weitere Briefbombe abgefangen</title>\n      ' \
             b'<link>https://www.swr.de/swraktuell/baden-wuerttemberg/heilbronn/briefbombe-am-flughafen-muenchen' \
             b'-abgefangen-100.html</link>\n      <pubDate>Thu, 18 Feb 2021 19:30:29 +0100</pubDate>\n      ' \
             b'<description>Nach Explosionen in der Lidl-Zentrale in Neckarsulm und einer weiteren Firma geht die ' \
             b'Polizei von einem Zusammenhang aus. Zuvor konnte eine dritte Sendung abgefangen werden. Sie war an ' \
             b'eine Lebensmittelfirma in Bayern adressiert.</description>\n      ' \
             b'<guid>https://www.swr.de/swraktuell/baden-wuerttemberg/heilbronn/briefbombe-am-flughafen-muenchen' \
             b'-abgefangen-100.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n             ' \
             b'   <a href="https://www.swr.de/swraktuell/baden-wuerttemberg/heilbronn/briefbombe-am-flughafen' \
             b'-muenchen-abgefangen-100.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/lidl-105~_v-mittel16x9.jpg" alt="Der abgesperrte ' \
             b'Haupteingang der Lidl Zentrale in Neckarsulm.| Bildquelle: dpa" /></a>\n                <br/>\n        ' \
             b'        <br/>\n            \n            Nach Explosionen in der Lidl-Zentrale in Neckarsulm und einer ' \
             b'weiteren Firma geht die Polizei von einem Zusammenhang aus. Zuvor konnte eine dritte Sendung ' \
             b'abgefangen werden. Sie war an eine Lebensmittelfirma in Bayern adressiert. <a ' \
             b'href="https://www.swr.de/swraktuell/baden-wuerttemberg/heilbronn/briefbombe-am-flughafen-muenchen' \
             b'-abgefangen-100.html">swr</a>\n        </p>\n        <ul>\n                \n            </ul>\n       ' \
             b' </p>\n        \n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>NATO weitet ' \
             b'Irak-Mission auf bis zu 4000 Soldaten aus</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/europa/nato-stoltenberg-afghanistan-irak-101.html</link>\n     ' \
             b' <pubDate>Thu, 18 Feb 2021 18:04:25 +0100</pubDate>\n      <description>Die Verteidigungsminister der ' \
             b'NATO-Mitglieder haben sich darauf geeinigt, die Irak-Mission auf bis zu 4000 Soldaten auszuweiten. ' \
             b'Eine Entscheidung \xc3\xbcber das m\xc3\xb6gliche Ende des Einsatzes in Afghanistan wurde hingegen ' \
             b'vertagt.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/europa/nato-stoltenberg-afghanistan-irak-101.html</guid>\n     ' \
             b' <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/nato-stoltenberg-afghanistan-irak-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/nato-afghanistan-117~_v-mittel16x9.jpg" ' \
             b'alt="US-Soldaten machen sich in Kundus zum Abflug in einem Hubschrauber vom Typ UH-60 Blackhawk ' \
             b'bereit.| Bildquelle: dpa" /></a>\n                <br/>\n                <br/>\n            \n         ' \
             b'   Die Verteidigungsminister der NATO-Mitglieder haben sich darauf geeinigt, die Irak-Mission auf bis ' \
             b'zu 4000 Soldaten auszuweiten. Eine Entscheidung \xc3\xbcber das m\xc3\xb6gliche Ende des Einsatzes in ' \
             b'Afghanistan wurde hingegen vertagt. <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/nato-stoltenberg-afghanistan-irak-101.html">mehr</a>\n  ' \
             b'      </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/europa/nato-stoltenberg-afghanistan-irak-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Marktbericht: Anleger scheuen das Risiko</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/finanzen/marktberichte/marktbericht-dax-dow-zinsen-101.html' \
             b'</link>\n      <pubDate>Thu, 18 Feb 2021 17:59:36 +0100</pubDate>\n      <description>An der ' \
             b'B\xc3\xb6rse geht es derzeit kaum vor oder zur\xc3\xbcck. Anleger schwanken zwischen ' \
             b'Konjunkturhoffnungen und Corona-Sorgen. Zu neuen Engagements ist keiner bereit.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/wirtschaft/finanzen/marktberichte/marktbericht-dax-dow-zinsen-101.html' \
             b'</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/finanzen/marktberichte/marktbericht-dax-dow-zinsen-101.html' \
             b'"><img src="https://www.tagesschau.de/wirtschaft/boerse/hr-boerse-image-19869~_v-mittel16x9.jpg" ' \
             b'alt="Deutsche B\xc3\xb6rse in Frankfurt" /></a>\n                <br/>\n                <br/>\n        ' \
             b'    \n            An der B\xc3\xb6rse geht es derzeit kaum vor oder zur\xc3\xbcck. Anleger schwanken ' \
             b'zwischen Konjunkturhoffnungen und Corona-Sorgen. Zu neuen Engagements ist keiner bereit. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/finanzen/marktberichte/marktbericht-dax-dow-zinsen-101.html' \
             b'">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        ' \
             b'<p><a href="https://www.tagesschau.de/wirtschaft/finanzen/marktberichte/marktbericht-dax-dow-zinsen' \
             b'-101.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    ' \
             b'<item>\n      <title>Wie der Einbruch bei Gesch\xc3\xa4ftsreisen dem Klima hilft</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/unternehmen/geschaeftsreisen-corona-101.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 17:47:03 +0100</pubDate>\n      <description>Auch weil so wenig ' \
             b'Gesch\xc3\xa4ftsreisen stattfinden, sind die CO2-Emissionen in Europa gesunken. Allerdings ist nicht ' \
             b'jede Videokonferenz unbedingt gut f\xc3\xbcr die Klimabilanz. Von Griet von ' \
             b'Petersdorff.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/wirtschaft/unternehmen/geschaeftsreisen-corona-101.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/geschaeftsreisen-corona-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/videokonferenz-105~_v-mittel16x9.jpg" alt="Split ' \
             b'Screen mit vielen zugeschalteten Gespr\xc3\xa4chspartnern| Bildquelle: AFP" /></a>\n                ' \
             b'<br/>\n                <br/>\n            \n            Auch weil so wenig Gesch\xc3\xa4ftsreisen ' \
             b'stattfinden, sind die CO2-Emissionen in Europa gesunken. Allerdings ist nicht jede Videokonferenz ' \
             b'unbedingt gut f\xc3\xbcr die Klimabilanz. Von Griet von Petersdorff. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/geschaeftsreisen-corona-101.html">mehr</a>\n    ' \
             b'    </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/geschaeftsreisen-corona-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>Wie ' \
             b'Ola K\xc3\xa4llenius Daimler umbaut</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/unternehmen/wie-ola-kaellenius-daimler-umbaut-101.html' \
             b'</link>\n      <pubDate>Thu, 18 Feb 2021 17:46:24 +0100</pubDate>\n      <description>Seit seinem ' \
             b'Amtsantritt im Mai 2019 hat Ola K\xc3\xa4llenius den Daimler-Konzern v\xc3\xb6llig umgekrempelt, ' \
             b'Tausende Arbeitspl\xc3\xa4tze gestrichen, neue Modelle angek\xc3\xbcndigt. Jetzt wird die Lkw-Sparte ' \
             b'abgespalten.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/wirtschaft/unternehmen/wie-ola-kaellenius-daimler-umbaut-101.html' \
             b'</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/wie-ola-kaellenius-daimler-umbaut-101.html' \
             b'"><img src="https://www.tagesschau.de/multimedia/bilder/kaellenius-103~_v-mittel16x9.jpg" alt="Der ' \
             b'neue Daimler-Chef Ole K\xc3\xa4llenius. | Bildquelle: dpa" /></a>\n                <br/>\n             ' \
             b'   <br/>\n            \n            Seit seinem Amtsantritt im Mai 2019 hat Ola K\xc3\xa4llenius den ' \
             b'Daimler-Konzern v\xc3\xb6llig umgekrempelt, Tausende Arbeitspl\xc3\xa4tze gestrichen, neue Modelle ' \
             b'angek\xc3\xbcndigt. Jetzt wird die Lkw-Sparte abgespalten. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/wie-ola-kaellenius-daimler-umbaut-101.html' \
             b'">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        ' \
             b'<p><a href="https://www.tagesschau.de/wirtschaft/unternehmen/wie-ola-kaellenius-daimler-umbaut-101' \
             b'.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    ' \
             b'<item>\n      <title>Gr\xc3\xbcnes Gespenst im Eigenheim</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/innenpolitik/gruene-eigenheim-debatte-101.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 17:11:54 +0100</pubDate>\n      <description>Durch die Mitte an die Macht: ' \
             b'Das ist der Kurs des Gr\xc3\xbcnen-Spitzenduos. Die Debatte ums Eigenheim passt ihnen da gar nicht ins ' \
             b'Konzept. Schlie\xc3\x9flich waren sie das Image der Verbotspartei gerade los. Von Corinna ' \
             b'Emundts.</description>\n      <guid>https://www.tagesschau.de/inland/innenpolitik/gruene-eigenheim' \
             b'-debatte-101.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                ' \
             b'<a href="https://www.tagesschau.de/inland/innenpolitik/gruene-eigenheim-debatte-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/habeck-baerbock-119~_v-mittel16x9.jpg" alt="Die ' \
             b'Bundesvorsitzenden von B\xc3\xbcndnis 90/Die Gr\xc3\xbcnen, Annalena Baerbock und Robert Habeck beim ' \
             b'digitalen politischen Aschermittwoch.| Bildquelle: dpa" /></a>\n                <br/>\n                ' \
             b'<br/>\n            \n            Durch die Mitte an die Macht: Das ist der Kurs des ' \
             b'Gr\xc3\xbcnen-Spitzenduos. Die Debatte ums Eigenheim passt ihnen da gar nicht ins Konzept. ' \
             b'Schlie\xc3\x9flich waren sie das Image der Verbotspartei gerade los. Von Corinna Emundts. <a ' \
             b'href="https://www.tagesschau.de/inland/innenpolitik/gruene-eigenheim-debatte-101.html">mehr</a>\n      ' \
             b'  </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/inland/innenpolitik/gruene-eigenheim-debatte-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>BioNTech/Pfizer wollten 54 Euro pro Dosis Impfstoff</title>\n      ' \
             b'<link>https://www.tagesschau.de/investigativ/ndr-wdr/corona-impfstoff-biontech-105.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 17:00:00 +0100</pubDate>\n      <description>Die Pharmaunternehmen Pfizer ' \
             b'und BioNTech wollten nach Informationen von NDR, WDR und "SZ" im Juni von der EU f\xc3\xbcr eine Dosis ' \
             b'Impfstoff 54,08 Euro. Der Arzneimittelchef der \xc3\x84rztekammer spricht von "unseri\xc3\xb6sem ' \
             b'Profitstreben".</description>\n      ' \
             b'<guid>https://www.tagesschau.de/investigativ/ndr-wdr/corona-impfstoff-biontech-105.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/investigativ/ndr-wdr/corona-impfstoff-biontech-105.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/impfstoff-127~_v-mittel16x9.jpg" ' \
             b'alt="Impfstoff-Fl\xc3\xa4schen von Biontech / Pfizer." /></a>\n                <br/>\n                ' \
             b'<br/>\n            \n            Die Pharmaunternehmen Pfizer und BioNTech wollten nach Informationen ' \
             b'von NDR, WDR und &quot;SZ&quot; im Juni von der EU f\xc3\xbcr eine Dosis Impfstoff 54,08 Euro. Der ' \
             b'Arzneimittelchef der \xc3\x84rztekammer spricht von &quot;unseri\xc3\xb6sem Profitstreben&quot;. <a ' \
             b'href="https://www.tagesschau.de/investigativ/ndr-wdr/corona-impfstoff-biontech-105.html">mehr</a>\n    ' \
             b'    </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/investigativ/ndr-wdr/corona-impfstoff-biontech-105.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Rettungseinsatz f\xc3\xbcr 4000 Meeresschildkr\xc3\xb6ten in Texas</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/amerika/schildkroeten-111.html</link>\n      <pubDate>Thu, ' \
             b'18 Feb 2021 16:46:41 +0100</pubDate>\n      <description>Schildkr\xc3\xb6ten sind nicht vor dem ' \
             b'Erfrieren gesch\xc3\xbctzt - auch wenn sie einen dicken Panzer haben. 4000 Meeresschildkr\xc3\xb6ten ' \
             b'wurden jetzt aus dem Golf von Mexiko gerettet und zum Aufw\xc3\xa4rmen in ein Tagungszentrum ' \
             b'gebracht.</description>\n      <guid>https://www.tagesschau.de/ausland/amerika/schildkroeten-111.html' \
             b'</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/amerika/schildkroeten-111.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/texas-schildkroeten-103~_v-mittel16x9.jpg" ' \
             b'alt="Meeresschildkr\xc3\xb6ten in einem Tagungszentrum in Texas| Bildquelle: dpa" /></a>\n             ' \
             b'   <br/>\n                <br/>\n            \n            Schildkr\xc3\xb6ten sind nicht vor dem ' \
             b'Erfrieren gesch\xc3\xbctzt - auch wenn sie einen dicken Panzer haben. 4000 Meeresschildkr\xc3\xb6ten ' \
             b'wurden jetzt aus dem Golf von Mexiko gerettet und zum Aufw\xc3\xa4rmen in ein Tagungszentrum gebracht. ' \
             b'<a href="https://www.tagesschau.de/ausland/amerika/schildkroeten-111.html">mehr</a>\n        </p>\n    ' \
             b'    <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/amerika/schildkroeten-111.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>AstraZeneca: "Um ' \
             b'Vielfaches besser als keine Impfung"</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/impfen-debatte-103.html</link>\n      <pubDate>Thu, 18 Feb 2021 ' \
             b'15:56:51 +0100</pubDate>\n      <description>Mit der Debatte um das AstraZeneca-Vakzin w\xc3\xa4chst ' \
             b'bei vielen die Skepsis. Tausende Impftermine bleiben frei. Experten betonen, der Impfstoff sei wirksam ' \
             b'und gut. Der SPD-Politiker Lauterbach will mit gutem Beispiel vorangehen.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/inland/impfen-debatte-103.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/inland/impfen-debatte-103.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/impfzentrum-nrw-101~_v-mittel16x9.jpg" alt="Ein ' \
             b'Impfzentrum in K\xc3\xb6ln (Archivbild).| Bildquelle: dpa" /></a>\n                <br/>\n             ' \
             b'   <br/>\n            \n            Mit der Debatte um das AstraZeneca-Vakzin w\xc3\xa4chst bei vielen ' \
             b'die Skepsis. Tausende Impftermine bleiben frei. Experten betonen, der Impfstoff sei wirksam und gut. ' \
             b'Der SPD-Politiker Lauterbach will mit gutem Beispiel vorangehen. <a ' \
             b'href="https://www.tagesschau.de/inland/impfen-debatte-103.html">mehr</a>\n        </p>\n        <ul>\n ' \
             b'               \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/inland/impfen-debatte-103.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>BGH-Beschluss: ' \
             b'Taschenrechner am Steuer ist verboten</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/bgh-taschenrechner-am-steuer-101.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 15:55:40 +0100</pubDate>\n      <description>Wer im Stra\xc3\x9fenverkehr ' \
             b'w\xc3\xa4hrend der Fahrt einen Taschenrechner bedient, muss mit einem Bu\xc3\x9fgeld rechnen. Das hat ' \
             b'nun der BGH klargestellt. Zwei Oberlandesgerichte konnten sich zuvor nicht auf eine Linie einigen. Von ' \
             b'Bernd Wolf.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/inland/bgh-taschenrechner-am-steuer-101.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/inland/bgh-taschenrechner-am-steuer-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/schlusslicht1374~_v-mittel16x9.jpg" ' \
             b'alt="Taschenrechner" /></a>\n                <br/>\n                <br/>\n            \n            ' \
             b'Wer im Stra\xc3\x9fenverkehr w\xc3\xa4hrend der Fahrt einen Taschenrechner bedient, muss mit einem ' \
             b'Bu\xc3\x9fgeld rechnen. Das hat nun der BGH klargestellt. Zwei Oberlandesgerichte konnten sich zuvor ' \
             b'nicht auf eine Linie einigen. Von Bernd Wolf. <a ' \
             b'href="https://www.tagesschau.de/inland/bgh-taschenrechner-am-steuer-101.html">mehr</a>\n        </p>\n ' \
             b'       <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/inland/bgh-taschenrechner-am-steuer-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Schlusslicht: Friseure in Lettland werden erfinderisch</title>\n      ' \
             b'<link>https://www.tagesschau.de/schlusslicht/lettland-haare-friseur-see-101.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 15:38:07 +0100</pubDate>\n      <description>Die Corona-Matte w\xc3\xa4chst ' \
             b'unaufh\xc3\xb6rlich: Nicht nur hierzulande, auch in anderen L\xc3\xa4ndern sind die Friseure ' \
             b'pandemiebedingt zu. In Lettland haben sich einige Friseure etwas einfallen lassen, um doch arbeiten zu ' \
             b'k\xc3\xb6nnen.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/schlusslicht/lettland-haare-friseur-see-101.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/schlusslicht/lettland-haare-friseur-see-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/riga-friseur-103~_v-mittel16x9.jpg" alt="Ein Friseur ' \
             b'schneidet am 15.02.2021 in Riga, Lettland, Haare auf dem zugefrorenen See Babelitis.| Bildquelle: AFP" ' \
             b'/></a>\n                <br/>\n                <br/>\n            \n            Die Corona-Matte ' \
             b'w\xc3\xa4chst unaufh\xc3\xb6rlich: Nicht nur hierzulande, auch in anderen L\xc3\xa4ndern sind die ' \
             b'Friseure pandemiebedingt zu. In Lettland haben sich einige Friseure etwas einfallen lassen, ' \
             b'um doch arbeiten zu k\xc3\xb6nnen. <a ' \
             b'href="https://www.tagesschau.de/schlusslicht/lettland-haare-friseur-see-101.html">mehr</a>\n        ' \
             b'</p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/schlusslicht/lettland-haare-friseur-see-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Folge der Corona-Pandemie: Weniger Asylantr\xc3\xa4ge in der EU</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/europa/eu-asylantraege-103.html</link>\n      <pubDate>Thu, ' \
             b'18 Feb 2021 15:34:22 +0100</pubDate>\n      <description>Die coronabedingten ' \
             b'Reisebeschr\xc3\xa4nkungen erschweren den Weg nach Europa. Deshalb ging auch die Zahl der ' \
             b'Asylantr\xc3\xa4ge 2020 deutlich zur\xc3\xbcck. An den Herkunftsl\xc3\xa4ndern der Schutzsuchenden ' \
             b'\xc3\xa4ndert sich hingegen kaum etwas.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/europa/eu-asylantraege-103.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eu-asylantraege-103.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/asyl-255~_v-mittel16x9.jpg" alt="Fl\xc3\xbcchtlinge ' \
             b'auf dem Weg nach Deutschland| Bildquelle: REUTERS" /></a>\n                <br/>\n                ' \
             b'<br/>\n            \n            Die coronabedingten Reisebeschr\xc3\xa4nkungen erschweren den Weg ' \
             b'nach Europa. Deshalb ging auch die Zahl der Asylantr\xc3\xa4ge 2020 deutlich zur\xc3\xbcck. An den ' \
             b'Herkunftsl\xc3\xa4ndern der Schutzsuchenden \xc3\xa4ndert sich hingegen kaum etwas. <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eu-asylantraege-103.html">mehr</a>\n        </p>\n      ' \
             b'  <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eu-asylantraege-103.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>EU leitet weiteres ' \
             b'Verfahren gegen Ungarn ein</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/europa/eu-ungarn-107.html</link>\n      <pubDate>Thu, ' \
             b'18 Feb 2021 15:33:34 +0100</pubDate>\n      <description>Die EU-Kommission leitet erneut ein ' \
             b'Vertragsverletzungsverfahren gegen Ungarn ein. Dabei geht es um die Rechte von ' \
             b'Nichtregierungsorganisationen - und diesmal k\xc3\xb6nnte es f\xc3\xbcr Budapest teuer werden. Von ' \
             b'Michael Schneider.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/europa/eu-ungarn-107.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eu-ungarn-107.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/ungarn-orban-eu-101~_v-mittel16x9.jpg" alt="Der ' \
             b'ungarische Ministerpr\xc3\xa4sident Orban richtet sich im Mai 2019 auf dem EU-Sondergipfel in ' \
             b'Br\xc3\xbcssel die Krawatte.| Bildquelle: dpa" /></a>\n                <br/>\n                <br/>\n  ' \
             b'          \n            Die EU-Kommission leitet erneut ein Vertragsverletzungsverfahren gegen Ungarn ' \
             b'ein. Dabei geht es um die Rechte von Nichtregierungsorganisationen - und diesmal k\xc3\xb6nnte es ' \
             b'f\xc3\xbcr Budapest teuer werden. Von Michael Schneider. <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eu-ungarn-107.html">mehr</a>\n        </p>\n        ' \
             b'<ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eu-ungarn-107.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Kryptow\xc3\xa4hrungen: Justiz hat Millionenverm\xc3\xb6gen in Bitcoins</title>\n      ' \
             b'<link>https://www.tagesschau.de/investigativ/wdr/bitcoin-159.html</link>\n      <pubDate>Thu, ' \
             b'18 Feb 2021 15:03:15 +0100</pubDate>\n      <description>Bundesweit haben Staatsanwaltschaften ' \
             b'Bitcoins beschlagnahmt, die inzwischen viele Millionen Euro wert sind. Manche Justizbeh\xc3\xb6rden ' \
             b'bunkern die Kryptow\xc3\xa4hrung, andere verkaufen sehr schnell. Von Florian Flade.</description>\n    ' \
             b'  <guid>https://www.tagesschau.de/investigativ/wdr/bitcoin-159.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/investigativ/wdr/bitcoin-159.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/bitcoin-161~_v-mittel16x9.jpg" alt="Bitcoin| ' \
             b'Bildquelle: EPA" /></a>\n                <br/>\n                <br/>\n            \n            ' \
             b'Bundesweit haben Staatsanwaltschaften Bitcoins beschlagnahmt, die inzwischen viele Millionen Euro wert ' \
             b'sind. Manche Justizbeh\xc3\xb6rden bunkern die Kryptow\xc3\xa4hrung, andere verkaufen sehr schnell. ' \
             b'Von Florian Flade. <a href="https://www.tagesschau.de/investigativ/wdr/bitcoin-159.html">mehr</a>\n    ' \
             b'    </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/investigativ/wdr/bitcoin-159.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>Das hat Elon Musk mit ' \
             b'dem SpaceX-Geld vor</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/technologie/spacex-starlink-elon-musk-starship-mars-101' \
             b'.html</link>\n      <pubDate>Thu, 18 Feb 2021 14:41:28 +0100</pubDate>\n      <description>Eine neue ' \
             b'Finanzierungsrunde hat die Bewertung des Raumfahrtunternehmens SpaceX auf 74 Milliarden Dollar in die ' \
             b'H\xc3\xb6he katapultiert. Doch wof\xc3\xbcr genau braucht Elon Musk eigentlich das ganze Geld? Von ' \
             b'Angela G\xc3\xb6pfert.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/wirtschaft/technologie/spacex-starlink-elon-musk-starship-mars-101' \
             b'.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/technologie/spacex-starlink-elon-musk-starship-mars-101' \
             b'.html"><img src="https://www.tagesschau.de/multimedia/bilder/elon-musk-121~_v-mittel16x9.jpg" ' \
             b'alt="Elon Musk auf einer Pressekonferenz nach dem erfolgreichen Start einer SpaceX-Rakete" /></a>\n    ' \
             b'            <br/>\n                <br/>\n            \n            Eine neue Finanzierungsrunde hat ' \
             b'die Bewertung des Raumfahrtunternehmens SpaceX auf 74 Milliarden Dollar in die H\xc3\xb6he ' \
             b'katapultiert. Doch wof\xc3\xbcr genau braucht Elon Musk eigentlich das ganze Geld? Von Angela ' \
             b'G\xc3\xb6pfert. <a href="https://www.tagesschau.de/wirtschaft/technologie/spacex-starlink-elon-musk' \
             b'-starship-mars-101.html">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n   ' \
             b'     </p>\n        <p><a href="https://www.tagesschau.de/wirtschaft/technologie/spacex-starlink-elon' \
             b'-musk-starship-mars-101.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n ' \
             b'   </item>\n    <item>\n      <title>Dubais K\xc3\xb6nigsfamilie: Gro\xc3\x9fbritannien sorgt sich um ' \
             b'Prinzessin Latifa</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/europa/uk-dubai-101.html</link>\n      <pubDate>Thu, ' \
             b'18 Feb 2021 14:22:06 +0100</pubDate>\n      <description>Ein paar kurze Videoclips w\xc3\xbchlen nicht ' \
             b'nur die britische Regierung auf: Sie stammen von Prinzessin Latifa aus Dubai, die von Gefangenschaft ' \
             b'und Todesangst spricht. Der Fall hat nun auch die UN erreicht.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/europa/uk-dubai-101.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/uk-dubai-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/latifa-101~_v-mittel16x9.jpg" alt="Screenshot aus dem ' \
             b'Video von Prinzessin Latifa| Bildquelle: dpa" /></a>\n                <br/>\n                <br/>\n   ' \
             b'         \n            Ein paar kurze Videoclips w\xc3\xbchlen nicht nur die britische Regierung auf: ' \
             b'Sie stammen von Prinzessin Latifa aus Dubai, die von Gefangenschaft und Todesangst spricht. Der Fall ' \
             b'hat nun auch die UN erreicht. <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/uk-dubai-101.html">mehr</a>\n        </p>\n        ' \
             b'<ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/europa/uk-dubai-101.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>Blackout in den USA: ' \
             b'Immer noch Hunderttausende ohne Strom</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/amerika/blackout-texas-usa-101.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 13:58:56 +0100</pubDate>\n      <description>Im S\xc3\xbcden der USA sind ' \
             b'immer noch Hunderttausende Menschen ohne Strom. Grund ist das au\xc3\x9fergew\xc3\xb6hnliche ' \
             b'Winterwetter, das eisige Temperaturen bis an den Golf von Mexiko bringt.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/amerika/blackout-texas-usa-101.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/amerika/blackout-texas-usa-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/stromausfall-111~_v-mittel16x9.jpg" alt="Ein dunkle ' \
             b'Stra\xc3\x9fe mit Wohnh\xc3\xa4usern in Argyle im US-Bundesstaat Texas" /></a>\n                ' \
             b'<br/>\n                <br/>\n            \n            Im S\xc3\xbcden der USA sind immer noch ' \
             b'Hunderttausende Menschen ohne Strom. Grund ist das au\xc3\x9fergew\xc3\xb6hnliche Winterwetter, ' \
             b'das eisige Temperaturen bis an den Golf von Mexiko bringt. <a ' \
             b'href="https://www.tagesschau.de/ausland/amerika/blackout-texas-usa-101.html">mehr</a>\n        </p>\n  ' \
             b'      <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/amerika/blackout-texas-usa-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Naturschutzrichtline: EU-Kommission verklagt Deutschland</title>\n      ' \
             b'<link>https://www.tagesschau.de/ausland/europa/eugh-naturschutz-klage-deutschland-101.html</link>\n    ' \
             b'  <pubDate>Thu, 18 Feb 2021 13:49:51 +0100</pubDate>\n      <description>Seit Jahren bem\xc3\xa4ngelt ' \
             b'die EU-Kommission, dass Bund und L\xc3\xa4nder systematisch zu wenig Naturschutzgebiete ausgewiesen ' \
             b'haben. Weil sich trotz der Mahnungen kaum etwas getan hat, klagt die Beh\xc3\xb6rde nun vor dem ' \
             b'Europ\xc3\xa4ischen Gerichtshof.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/europa/eugh-naturschutz-klage-deutschland-101.html</guid>\n    ' \
             b'  <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eugh-naturschutz-klage-deutschland-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/naturschutzgebiet-103~_v-mittel16x9.jpg" alt="Ein ' \
             b'Schild weist auf ein Naturschutzgebiet hin. | Bildquelle: dpa" /></a>\n                <br/>\n         ' \
             b'       <br/>\n            \n            Seit Jahren bem\xc3\xa4ngelt die EU-Kommission, dass Bund und ' \
             b'L\xc3\xa4nder systematisch zu wenig Naturschutzgebiete ausgewiesen haben. Weil sich trotz der ' \
             b'Mahnungen kaum etwas getan hat, klagt die Beh\xc3\xb6rde nun vor dem Europ\xc3\xa4ischen Gerichtshof. ' \
             b'<a href="https://www.tagesschau.de/ausland/europa/eugh-naturschutz-klage-deutschland-101.html">mehr</a' \
             b'>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/europa/eugh-naturschutz-klage-deutschland-101.html">Meldung ' \
             b'bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>AfD in Baden-W\xc3\xbcrttemberg: Extrem rechts im Wahlkampf</title>\n      ' \
             b'<link>https://www.tagesschau.de/investigativ/monitor/afd-abgeordnete-103.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 13:45:52 +0100</pubDate>\n      <description>Im Landtagswahlkampf in ' \
             b'Baden-W\xc3\xbcrttemberg fallen mehrere AfD-Kandidaten mit Rassismus, Verschw\xc3\xb6rungsglauben und ' \
             b'rechtsideologischen \xc3\x84u\xc3\x9ferungen auf. Die Partei tut sich schwer, gegen extrem rechte ' \
             b'Mitglieder vorzugehen.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/investigativ/monitor/afd-abgeordnete-103.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/investigativ/monitor/afd-abgeordnete-103.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/afd-logo-115~_v-mittel16x9.jpg" alt="Papierfahnen mit ' \
             b'dem AFD-Logo liegen auf einem Tisch| Bildquelle: dpa" /></a>\n                <br/>\n                ' \
             b'<br/>\n            \n            Im Landtagswahlkampf in Baden-W\xc3\xbcrttemberg fallen mehrere ' \
             b'AfD-Kandidaten mit Rassismus, Verschw\xc3\xb6rungsglauben und rechtsideologischen ' \
             b'\xc3\x84u\xc3\x9ferungen auf. Die Partei tut sich schwer, gegen extrem rechte Mitglieder vorzugehen. ' \
             b'<a href="https://www.tagesschau.de/investigativ/monitor/afd-abgeordnete-103.html">mehr</a>\n        ' \
             b'</p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/investigativ/monitor/afd-abgeordnete-103.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>Jede ' \
             b'dritte Firma zur Kurzarbeit gezwungen</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/konjunktur/jede-dritte-firma-zur-kurzarbeit-gezwungen-101' \
             b'.html</link>\n      <pubDate>Thu, 18 Feb 2021 13:30:24 +0100</pubDate>\n      <description>Eine ' \
             b'aktuelle Studie des Ifo-Instituts hat ergeben, dass rund ein Drittel aller Unternehmen auf Kurzarbeit ' \
             b'zur\xc3\xbcckgreifen muss. Besonders hart trifft es die Reisebranche und Gastronomie.</description>\n  ' \
             b'    <guid>https://www.tagesschau.de/wirtschaft/konjunktur/jede-dritte-firma-zur-kurzarbeit-gezwungen' \
             b'-101.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/konjunktur/jede-dritte-firma-zur-kurzarbeit-gezwungen-101' \
             b'.html"><img src="https://www.tagesschau.de/multimedia/bilder/kurzarbeit-131~_v-mittel16x9.jpg" ' \
             b'alt="Zwei Kugelschreiber liegen auf einem Antragsformular f\xc3\xbcr Kurzarbeitergeld (gestellte ' \
             b'Szene). | Bildquelle: dpa" /></a>\n                <br/>\n                <br/>\n            \n        ' \
             b'    Eine aktuelle Studie des Ifo-Instituts hat ergeben, dass rund ein Drittel aller Unternehmen auf ' \
             b'Kurzarbeit zur\xc3\xbcckgreifen muss. Besonders hart trifft es die Reisebranche und Gastronomie. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/konjunktur/jede-dritte-firma-zur-kurzarbeit-gezwungen-101' \
             b'.html">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n       ' \
             b' <p><a href="https://www.tagesschau.de/wirtschaft/konjunktur/jede-dritte-firma-zur-kurzarbeit' \
             b'-gezwungen-101.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    ' \
             b'</item>\n    <item>\n      <title>Politik ringt um Gesetz gegen Hass im Netz</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/gesetz-gegen-hasskriminalitaet-101.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 13:18:52 +0100</pubDate>\n      <description>Nach dem rassistischen Anschlag ' \
             b'in Hanau hat die Regierung Hass im Netz den Kampf angesagt - und der Bundestag schon 2020 ein Gesetz ' \
             b'dazu verabschiedet. Aber es ist immer noch nicht in Kraft und die Ungeduld w\xc3\xa4chst. Von ' \
             b'Bj\xc3\xb6rn Dake.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/inland/gesetz-gegen-hasskriminalitaet-101.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/inland/gesetz-gegen-hasskriminalitaet-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/gesetz-gegen-hass-im-netz-101~_v-mittel16x9.jpg" ' \
             b'alt="Blick in den Bundestag| Bildquelle: dpa" /></a>\n                <br/>\n                <br/>\n   ' \
             b'         \n            Nach dem rassistischen Anschlag in Hanau hat die Regierung Hass im Netz den ' \
             b'Kampf angesagt - und der Bundestag schon 2020 ein Gesetz dazu verabschiedet. Aber es ist immer noch ' \
             b'nicht in Kraft und die Ungeduld w\xc3\xa4chst. Von Bj\xc3\xb6rn Dake. <a ' \
             b'href="https://www.tagesschau.de/inland/gesetz-gegen-hasskriminalitaet-101.html">mehr</a>\n        ' \
             b'</p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/inland/gesetz-gegen-hasskriminalitaet-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Hamburger Rechtsmediziner: Coronavirus meistens Todesursache</title>\n      ' \
             b'<link>https://www.ndr.de/nachrichten/hamburg/coronavirus/Studie-zu-Corona-Toten-Virus-in-meisten' \
             b'-Faellen-todesursaechlich,rechtsmedizin214.html</link>\n      <pubDate>Thu, 18 Feb 2021 13:00:16 ' \
             b'+0100</pubDate>\n      <description>Hamburger Rechtsmediziner haben von Beginn der Pandemie an die ' \
             b'Todesursache Verstorbener untersucht. Nach 735 Obduktionen stellten sie fest, dass das Coronavirus ' \
             b'todesurs\xc3\xa4chlich war.</description>\n      ' \
             b'<guid>https://www.ndr.de/nachrichten/hamburg/coronavirus/Studie-zu-Corona-Toten-Virus-in-meisten' \
             b'-Faellen-todesursaechlich,rechtsmedizin214.html</guid>\n      <content:encoded><![CDATA[\n        ' \
             b'<p>\n            \n                <a ' \
             b'href="https://www.ndr.de/nachrichten/hamburg/coronavirus/Studie-zu-Corona-Toten-Virus-in-meisten' \
             b'-Faellen-todesursaechlich,rechtsmedizin214.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/uke-corona-101~_v-mittel16x9.jpg" alt="UKE in ' \
             b'Hamburg| Bildquelle: dpa" /></a>\n                <br/>\n                <br/>\n            \n         ' \
             b'   Hamburger Rechtsmediziner haben von Beginn der Pandemie an die Todesursache Verstorbener ' \
             b'untersucht. Nach 735 Obduktionen stellten sie fest, dass das Coronavirus todesurs\xc3\xa4chlich war. ' \
             b'<a href="https://www.ndr.de/nachrichten/hamburg/coronavirus/Studie-zu-Corona-Toten-Virus-in-meisten' \
             b'-Faellen-todesursaechlich,rechtsmedizin214.html">ndr</a>\n        </p>\n        <ul>\n                ' \
             b'\n            </ul>\n        </p>\n        \n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Clan-Kriminalit\xc3\xa4t: Razzien in Berlin und Brandenburg</title>\n      ' \
             b'<link>https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans-kriminalitaet' \
             b'-grosseinsatz-razzia-polizei-lka.html</link>\n      <pubDate>Thu, 18 Feb 2021 12:42:51 ' \
             b'+0100</pubDate>\n      <description>Es geht um Waffen-, Drogen- und Sprengstoffhandel: Hunderte ' \
             b'Spezialeinsatzkr\xc3\xa4fte durchsuchen mehr als 20 Wohnungen und H\xc3\xa4user einer Berliner ' \
             b'Gro\xc3\x9ffamilie, die dem Clanmilieu zugerechnet wird. Mindestens zwei Verd\xc3\xa4chtige wurden ' \
             b'festgenommen.</description>\n      ' \
             b'<guid>https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans-kriminalitaet' \
             b'-grosseinsatz-razzia-polizei-lka.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n          ' \
             b'  \n                <a href="https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans' \
             b'-kriminalitaet-grosseinsatz-razzia-polizei-lka.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/polizisten-razzia-103~_v-mittel16x9.jpg" ' \
             b'alt="Polizisten gehen bei einer Razzia mit einem Hund in ein Haus.| Bildquelle: picture alliance/dpa" ' \
             b'/></a>\n                <br/>\n                <br/>\n            \n            Es geht um Waffen-, ' \
             b'Drogen- und Sprengstoffhandel: Hunderte Spezialeinsatzkr\xc3\xa4fte durchsuchen mehr als 20 Wohnungen ' \
             b'und H\xc3\xa4user einer Berliner Gro\xc3\x9ffamilie, die dem Clanmilieu zugerechnet wird. Mindestens ' \
             b'zwei Verd\xc3\xa4chtige wurden festgenommen. <a ' \
             b'href="https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans-kriminalitaet' \
             b'-grosseinsatz-razzia-polizei-lka.html">rbb</a>\n        </p>\n        <ul>\n                \n         ' \
             b'   </ul>\n        </p>\n        \n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Klingbeil ein Jahr nach Hanau: "Wir sind alle in der Verantwortung"</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/innenpolitik/anschlag-hanau-rassismus-klingbeil-101.html</link' \
             b'>\n      <pubDate>Thu, 18 Feb 2021 12:23:12 +0100</pubDate>\n      <description>Deutschland habe ein ' \
             b'wachsendes Rassismusproblem, sagt SPD-Generalsekret\xc3\xa4r Klingbeil. Ein Jahr nach dem Anschlag von ' \
             b'Hanau wurde politisch zwar einiges auf den Weg gebracht - aber: "Nazis m\xc3\xbcssen auf vielen Ebenen ' \
             b'bek\xc3\xa4mpft werden."</description>\n      ' \
             b'<guid>https://www.tagesschau.de/inland/innenpolitik/anschlag-hanau-rassismus-klingbeil-101.html</guid' \
             b'>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/inland/innenpolitik/anschlag-hanau-rassismus-klingbeil-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/klingbeil-121~_v-mittel16x9.jpg" ' \
             b'alt="SPD-Generalsekret\xc3\xa4r Lars Klingbeil| Bildquelle: dpa" /></a>\n                <br/>\n       ' \
             b'         <br/>\n            \n            Deutschland habe ein wachsendes Rassismusproblem, ' \
             b'sagt SPD-Generalsekret\xc3\xa4r Klingbeil. Ein Jahr nach dem Anschlag von Hanau wurde politisch zwar ' \
             b'einiges auf den Weg gebracht - aber: &quot;Nazis m\xc3\xbcssen auf vielen Ebenen bek\xc3\xa4mpft ' \
             b'werden.&quot; <a href="https://www.tagesschau.de/inland/innenpolitik/anschlag-hanau-rassismus' \
             b'-klingbeil-101.html">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n       ' \
             b' </p>\n        <p><a href="https://www.tagesschau.de/inland/innenpolitik/anschlag-hanau-rassismus' \
             b'-klingbeil-101.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    ' \
             b'</item>\n    <item>\n      <title>Kinderheim in Corona-Zeiten: Abschottung statt Trost</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/gesellschaft/tt-mittendrin-kinderheim-corona-101.html</link>\n  ' \
             b'    <pubDate>Thu, 18 Feb 2021 12:19:44 +0100</pubDate>\n      <description>Einen Corona-Ausbruch hat ' \
             b'das Kinderheim "Monikahaus" schon hinter sich - die Sorge vor einem zweiten ist gro\xc3\x9f. Aber die ' \
             b'Vorsichtsma\xc3\x9fnahmen passen nicht zum N\xc3\xa4hebed\xc3\xbcrfnis traumatisierter Kinder. Von ' \
             b'Rick Gajek.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/inland/gesellschaft/tt-mittendrin-kinderheim-corona-101.html</guid>\n  ' \
             b'    <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/inland/gesellschaft/tt-mittendrin-kinderheim-corona-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/kinderheim-frankfurt-111~_v-mittel16x9.jpg" ' \
             b'alt="Einblick in Zimmer| Bildquelle: Rick Gajek" /></a>\n                <br/>\n                ' \
             b'<br/>\n            \n            Einen Corona-Ausbruch hat das Kinderheim &quot;Monikahaus&quot; schon ' \
             b'hinter sich - die Sorge vor einem zweiten ist gro\xc3\x9f. Aber die Vorsichtsma\xc3\x9fnahmen passen ' \
             b'nicht zum N\xc3\xa4hebed\xc3\xbcrfnis traumatisierter Kinder. Von Rick Gajek. <a ' \
             b'href="https://www.tagesschau.de/inland/gesellschaft/tt-mittendrin-kinderheim-corona-101.html">mehr</a' \
             b'>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/inland/gesellschaft/tt-mittendrin-kinderheim-corona-101.html">Meldung ' \
             b'bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Kommentar zu AstraZeneca: "Was f\xc3\xbcr ein Luxusproblem!"</title>\n      ' \
             b'<link>https://www.tagesschau.de/kommentar/astrazeneca-123.html</link>\n      <pubDate>Thu, 18 Feb 2021 ' \
             b'12:16:17 +0100</pubDate>\n      <description>Impfstoffe sind der Weg aus der Corona-Krise. Trotzdem ' \
             b'wollen sich viele Deutsche lieber gar nicht impfen lassen als mit dem Pr\xc3\xa4parat von AstraZeneca ' \
             b'- ein gef\xc3\xa4hrliches Luxusproblem, meint Evi Seibert.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/kommentar/astrazeneca-123.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/kommentar/astrazeneca-123.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/astra-zeneca-115~_v-mittel16x9.jpg" ' \
             b'alt="Beh\xc3\xa4lter mit dem Impfstoff Astra Zeneca| Bildquelle: AP" /></a>\n                <br/>\n   ' \
             b'             <br/>\n            \n            Impfstoffe sind der Weg aus der Corona-Krise. Trotzdem ' \
             b'wollen sich viele Deutsche lieber gar nicht impfen lassen als mit dem Pr\xc3\xa4parat von AstraZeneca ' \
             b'- ein gef\xc3\xa4hrliches Luxusproblem, meint Evi Seibert. <a ' \
             b'href="https://www.tagesschau.de/kommentar/astrazeneca-123.html">mehr</a>\n        </p>\n        <ul>\n ' \
             b'               \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/kommentar/astrazeneca-123.html">Meldung bei www.tagesschau.de ' \
             b'lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>Wie weit ist die ' \
             b'Batterieforschung?</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/akkuforschung-batterien-101.html</link>\n      ' \
             b'<pubDate>Thu, 18 Feb 2021 12:12:46 +0100</pubDate>\n      <description>Im Alltag leistet die Batterie ' \
             b'gute Dienste. Nur f\xc3\xbcr Zukunftsthemen wie E-Mobilit\xc3\xa4t oder Energiewende fehlt ihr noch ' \
             b'der Saft. Aber Wissenschaft und Wirtschaft arbeiten an L\xc3\xb6sungen. Von Juri ' \
             b'Sonnenholzner.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/wirtschaft/akkuforschung-batterien-101.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/akkuforschung-batterien-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/akasol-batterie-101~_v-mittel16x9.jpg" ' \
             b'alt="Akasol-Autobatterie" /></a>\n                <br/>\n                <br/>\n            \n         ' \
             b'   Im Alltag leistet die Batterie gute Dienste. Nur f\xc3\xbcr Zukunftsthemen wie E-Mobilit\xc3\xa4t ' \
             b'oder Energiewende fehlt ihr noch der Saft. Aber Wissenschaft und Wirtschaft arbeiten an ' \
             b'L\xc3\xb6sungen. Von Juri Sonnenholzner. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/akkuforschung-batterien-101.html">mehr</a>\n        </p>\n  ' \
             b'      <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/wirtschaft/akkuforschung-batterien-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Entwurf zum Lieferkettengesetz: Meilenstein oder Papiertiger?</title>\n      ' \
             b'<link>https://www.tagesschau.de/investigativ/monitor/lobbyismus-lieferketten-gesetz-101.html</link>\n  ' \
             b'    <pubDate>Thu, 18 Feb 2021 11:31:01 +0100</pubDate>\n      <description>Die Regierung spricht von ' \
             b'einem "historischen Durchbruch". Doch beim Entwurf des Lieferkettengesetzes haben sich in zentralen ' \
             b'Punkten Wirtschaftsverb\xc3\xa4nde durchgesetzt. Von S. Laghai und N. Steiner.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/investigativ/monitor/lobbyismus-lieferketten-gesetz-101.html</guid>\n  ' \
             b'    <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/investigativ/monitor/lobbyismus-lieferketten-gesetz-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/bangladesch-naeherinnen-101~_v-mittel16x9.jpg" ' \
             b'alt="N\xc3\xa4herinnen in einer Textilfabrik in Bangladesch| Bildquelle: dpa" /></a>\n                ' \
             b'<br/>\n                <br/>\n            \n            Die Regierung spricht von einem ' \
             b'&quot;historischen Durchbruch&quot;. Doch beim Entwurf des Lieferkettengesetzes haben sich in ' \
             b'zentralen Punkten Wirtschaftsverb\xc3\xa4nde durchgesetzt. Von S. Laghai und N. Steiner. <a ' \
             b'href="https://www.tagesschau.de/investigativ/monitor/lobbyismus-lieferketten-gesetz-101.html">mehr</a' \
             b'>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/investigativ/monitor/lobbyismus-lieferketten-gesetz-101.html">Meldung ' \
             b'bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Flugzeugbauer Airbus macht Milliardenverlust</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/unternehmen/airbus-macht-milliardenverlust-101.html</link' \
             b'>\n      <pubDate>Thu, 18 Feb 2021 11:24:42 +0100</pubDate>\n      <description>Der Einbruch des ' \
             b'Flugverkehrs hinterl\xc3\xa4sst tiefe Spuren beim europ\xc3\xa4ischen Luft- und Raumfahrtkonzern ' \
             b'Airbus: Der Umsatz bricht ein, unter dem Strich steht ein Milliardenverlust.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/wirtschaft/unternehmen/airbus-macht-milliardenverlust-101.html</guid' \
             b'>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/airbus-macht-milliardenverlust-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/airbus-301~_v-mittel16x9.jpg" alt="Ein Flugzeug ' \
             b'steigt \xc3\xbcber einem Airbus-Geb\xc3\xa4ude in Toulouse in die Luft| Bildquelle: Airbus" /></a>\n   ' \
             b'             <br/>\n                <br/>\n            \n            Der Einbruch des Flugverkehrs ' \
             b'hinterl\xc3\xa4sst tiefe Spuren beim europ\xc3\xa4ischen Luft- und Raumfahrtkonzern Airbus: Der Umsatz ' \
             b'bricht ein, unter dem Strich steht ein Milliardenverlust. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/airbus-macht-milliardenverlust-101.html">mehr' \
             b'</a>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/airbus-macht-milliardenverlust-101.html' \
             b'">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n    ' \
             b'  <title>Was Bio-Siegel verraten - und was nicht</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/verbraucher/bio-siegel-oeko-lebensmittel-verbraucherschutz' \
             b'-101.html</link>\n      <pubDate>Thu, 18 Feb 2021 10:06:49 +0100</pubDate>\n      <description>Immer ' \
             b'mehr Menschen ern\xc3\xa4hren sich gesund, regional und nachhaltig. Der Appetit auf Bio-Produkte ' \
             b'steigt. Welchen Siegeln k\xc3\xb6nnen Verbraucher vertrauen? Und wie aussagekr\xc3\xa4ftig sind sie? ' \
             b'Von Till B\xc3\xbccker.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/wirtschaft/verbraucher/bio-siegel-oeko-lebensmittel-verbraucherschutz' \
             b'-101.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/verbraucher/bio-siegel-oeko-lebensmittel-verbraucherschutz' \
             b'-101.html"><img src="https://www.tagesschau.de/multimedia/bilder/bild-331~_v-mittel16x9.jpg" ' \
             b'alt="Bio-Siegel auf Avocados" /></a>\n                <br/>\n                <br/>\n            \n     ' \
             b'       Immer mehr Menschen ern\xc3\xa4hren sich gesund, regional und nachhaltig. Der Appetit auf ' \
             b'Bio-Produkte steigt. Welchen Siegeln k\xc3\xb6nnen Verbraucher vertrauen? Und wie ' \
             b'aussagekr\xc3\xa4ftig sind sie? Von Till B\xc3\xbccker. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/verbraucher/bio-siegel-oeko-lebensmittel-verbraucherschutz' \
             b'-101.html">mehr</a>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n   ' \
             b'     <p><a href="https://www.tagesschau.de/wirtschaft/verbraucher/bio-siegel-oeko-lebensmittel' \
             b'-verbraucherschutz-101.html">Meldung bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n  ' \
             b'  </item>\n    <item>\n      <title>Belarus: Zwei Jahre Haft f\xc3\xbcr Minsker ' \
             b'Reporterinnen</title>\n      <link>https://www.tagesschau.de/ausland/europa/belarus-journalistinnen' \
             b'-belsat-101.html</link>\n      <pubDate>Thu, 18 Feb 2021 10:05:18 +0100</pubDate>\n      ' \
             b'<description>Zwei Reporterinnen des Senders Belsat sind in Minsk zu zwei Jahren Haft verurteilt ' \
             b'worden. Der Vorwurf: Sie h\xc3\xa4tten Proteste organisiert. Die beiden hatten von einer Demonstration ' \
             b'per Livestream berichtet.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/ausland/europa/belarus-journalistinnen-belsat-101.html</guid>\n      ' \
             b'<content:encoded><![CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/belarus-journalistinnen-belsat-101.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/belarus-belsat-haft-101~_v-mittel16x9.jpg" alt="Die ' \
             b'belarusischen Reporterinnen Katsiaryna Andreyeva and Darya Chultsova| Bildquelle: REUTERS" /></a>\n    ' \
             b'            <br/>\n                <br/>\n            \n            Zwei Reporterinnen des Senders ' \
             b'Belsat sind in Minsk zu zwei Jahren Haft verurteilt worden. Der Vorwurf: Sie h\xc3\xa4tten Proteste ' \
             b'organisiert. Die beiden hatten von einer Demonstration per Livestream berichtet. <a ' \
             b'href="https://www.tagesschau.de/ausland/europa/belarus-journalistinnen-belsat-101.html">mehr</a>\n     ' \
             b'   </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/ausland/europa/belarus-journalistinnen-belsat-101.html">Meldung bei ' \
             b'www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      <title>Auf ' \
             b'AstraZeneca sollte mRNA-Impfstoff folgen</title>\n      ' \
             b'<link>https://www.tagesschau.de/inland/astrazeneca-impfung-103.html</link>\n      <pubDate>Thu, ' \
             b'18 Feb 2021 09:31:43 +0100</pubDate>\n      <description>Wer mit AstraZeneca gegen Corona geimpft ' \
             b'wird, sollte sp\xc3\xa4ter ein mRNA-Vakzin erhalten. Das sollte garantiert werden, empfiehlt der ' \
             b'Verband der Immunologen. Es k\xc3\xb6nnte nicht nur die Wirkung verst\xc3\xa4rken, sondern auch die ' \
             b'Akzeptanz erh\xc3\xb6hen.</description>\n      ' \
             b'<guid>https://www.tagesschau.de/inland/astrazeneca-impfung-103.html</guid>\n      <content:encoded><![' \
             b'CDATA[\n        <p>\n            \n                <a ' \
             b'href="https://www.tagesschau.de/inland/astrazeneca-impfung-103.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/astrazeneca-moderna-biontech-101~_v-mittel16x9.jpg" ' \
             b'alt="Impfstoffe von BioNTech, Moderna und AstraZeneca| Bildquelle: REUTERS" /></a>\n                ' \
             b'<br/>\n                <br/>\n            \n            Wer mit AstraZeneca gegen Corona geimpft wird, ' \
             b'sollte sp\xc3\xa4ter ein mRNA-Vakzin erhalten. Das sollte garantiert werden, empfiehlt der Verband der ' \
             b'Immunologen. Es k\xc3\xb6nnte nicht nur die Wirkung verst\xc3\xa4rken, sondern auch die Akzeptanz ' \
             b'erh\xc3\xb6hen. <a href="https://www.tagesschau.de/inland/astrazeneca-impfung-103.html">mehr</a>\n     ' \
             b'   </p>\n        <ul>\n                \n            </ul>\n        </p>\n        \n    ' \
             b']]></content:encoded>\n    </item>\n    <item>\n      <title>US-Flugaufsicht ordnet Inspektion des ' \
             b'Boeing 787 Dreamliner an</title>\n      ' \
             b'<link>https://www.tagesschau.de/wirtschaft/unternehmen/boeing-787-dreamliner-737-max-101.html</link>\n ' \
             b'     <pubDate>Thu, 18 Feb 2021 09:21:09 +0100</pubDate>\n      <description>N\xc3\xa4chste ' \
             b'Hiobsbotschaft f\xc3\xbcr Boeing: Nach dem 737-Max-Debakel hat die US-Luftfahrtaufsicht nun die ' \
             b'Inspektion des Langstreckenjets 787 Dreamliner angeordnet. Ein Defekt k\xc3\xb6nne fatale Folgen ' \
             b'haben.</description>\n      <guid>https://www.tagesschau.de/wirtschaft/unternehmen/boeing-787' \
             b'-dreamliner-737-max-101.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n            \n     ' \
             b'           <a href="https://www.tagesschau.de/wirtschaft/unternehmen/boeing-787-dreamliner-737-max-101' \
             b'.html"><img src="https://www.tagesschau.de/multimedia/bilder/boeing-dreamliner-101~_v-mittel16x9.jpg" ' \
             b'alt="Eine Boeing 787-10 &quot;Dreamliner&quot; steht auf dem Charleston International Airport. (' \
             b'M\xc3\xa4rz 2017)| Bildquelle: dpa" /></a>\n                <br/>\n                <br/>\n            ' \
             b'\n            N\xc3\xa4chste Hiobsbotschaft f\xc3\xbcr Boeing: Nach dem 737-Max-Debakel hat die ' \
             b'US-Luftfahrtaufsicht nun die Inspektion des Langstreckenjets 787 Dreamliner angeordnet. Ein Defekt ' \
             b'k\xc3\xb6nne fatale Folgen haben. <a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/boeing-787-dreamliner-737-max-101.html">mehr</a' \
             b'>\n        </p>\n        <ul>\n                \n            </ul>\n        </p>\n        <p><a ' \
             b'href="https://www.tagesschau.de/wirtschaft/unternehmen/boeing-787-dreamliner-737-max-101.html">Meldung ' \
             b'bei www.tagesschau.de lesen</a></p>\n    ]]></content:encoded>\n    </item>\n    <item>\n      ' \
             b'<title>Clan-Kriminalit\xc3\xa4t: Razzien in Berlin und Brandenburg</title>\n      ' \
             b'<link>https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans-kriminalitaet' \
             b'-grosseinsatz-razzia-polizei-lka.html</link>\n      <pubDate>Thu, 18 Feb 2021 09:03:49 ' \
             b'+0100</pubDate>\n      <description>Es geht um Waffen-, Drogen- und Sprengstoffhandel: Hunderte ' \
             b'Spezialeinsatzkr\xc3\xa4fte durchsuchen mehr als 20 Wohnungen und H\xc3\xa4user einer Berliner ' \
             b'Gro\xc3\x9ffamilie, die dem Clanmilieu zugerechnet wird. Mindestens zwei Verd\xc3\xa4chtige wurden ' \
             b'festgenommen.</description>\n      ' \
             b'<guid>https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans-kriminalitaet' \
             b'-grosseinsatz-razzia-polizei-lka.html</guid>\n      <content:encoded><![CDATA[\n        <p>\n          ' \
             b'  \n                <a href="https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans' \
             b'-kriminalitaet-grosseinsatz-razzia-polizei-lka.html"><img ' \
             b'src="https://www.tagesschau.de/multimedia/bilder/polizisten-razzia-103~_v-mittel16x9.jpg" ' \
             b'alt="Polizisten gehen bei einer Razzia mit einem Hund in ein Haus.| Bildquelle: picture alliance/dpa" ' \
             b'/></a>\n                <br/>\n                <br/>\n            \n            Es geht um Waffen-, ' \
             b'Drogen- und Sprengstoffhandel: Hunderte Spezialeinsatzkr\xc3\xa4fte durchsuchen mehr als 20 Wohnungen ' \
             b'und H\xc3\xa4user einer Berliner Gro\xc3\x9ffamilie, die dem Clanmilieu zugerechnet wird. Mindestens ' \
             b'zwei Verd\xc3\xa4chtige wurden festgenommen. <a ' \
             b'href="https://www.rbb24.de/panorama/beitrag/2021/02/berlin-brandenburg-clans-kriminalitaet' \
             b'-grosseinsatz-razzia-polizei-lka.html">rbb</a>\n        </p>\n        <ul>\n                \n         ' \
             b'   </ul>\n        </p>\n        \n    ]]></content:encoded>\n    </item>\n  </channel>\n</rss>\n '
        mock__getResponse.return_value = ml
        res1 = inst.getArticleList()
        expected_res1 = [{'title': 'NASA-Rover "Perseverance" gelingt Mars-Landung',
                          'description': 'Der NASA-Rover "Perseverance" ist nach sechs Monaten Flugzeit erfolgreich '
                                         'auf dem Mars gelandet. Er soll mehrere Jahre lang nach Spuren früheren '
                                         'mikrobiellen Lebens suchen. Außerdem wird er das Klima und die Geologie des '
                                         'Planeten erforschen.'},
                         {'title': 'PEI bewertet AstraZeneca-Vakzin weiter positiv',
                          'description': 'Impfreaktionen, Krankschreibungen und geplatzte Impftermine - das '
                                         'AstraZeneca-Vakzin hat für Diskussionen gesorgt. Das Paul-Ehrlich-Institut '
                                         'hält den Impfstoff weiter für wirksam und sicher. Ärzte und Politiker '
                                         'versuchen Vertrauen zu schaffen.'},
                         {'title': 'Livestream: Die Marslandung von "Perserverance"',
                          'description': 'Nach rund sechs Monaten Flugzeit landet der US-Rover "Perseverance" auf dem '
                                         'Mars landen. Sehen Sie das Landemanöver und die ersten Bilder vom roten '
                                         'Planeten hier live.'},
                         {'title': 'Leverkusen verliert nach furioser Aufholjagd gegen Bern',
                          'description': 'Nach einer extrem schwachen ersten Halbzeit glich Leverkusen im Europa '
                                         'League-Spiel gegen Bern einen 0:3 Rückstand aus. Doch ein später Treffer '
                                         'der Schweizer machte die Aufholjagd zunichte.'},
                         {'title': 'Proteste in Myanmar: Hackerangriffe und Straßenblockaden',
                          'description': 'Die Proteste in Myanmar gegen die Militärjunta nehmen neue Formen an: Autos und Motorräder blockieren die Straßen, Hacker greifen Webseiten der Armee an. Auch der internationale Druck auf das Militär steigt.'}]
        self.assertEqual(expected_res1, res1)

    @patch('news_wrapper.NewsScraper._getResponse')
    def test_get_article_list2(self, mock__getResponse):
        inst = NewsScraper.getInstance('http://127.0.0.1')
        mock__getResponse.return_value = []
        res2 = inst.getArticleList()
        expected_res2 = None
        self.assertEqual(expected_res2, res2)

    @patch('news_wrapper.NewsScraper._getResponse')
    def test_get_article_list3(self, mock__getResponse):
        inst = NewsScraper.getInstance('http://127.0.0.1')
        mock__getResponse.return_value = None
        res3 = inst.getArticleList()
        expected_res3 = None
        self.assertEqual(expected_res3, res3)

    @patch('news_wrapper.NewsScraper._getResponse')
    def test_get_article_list4(self, mock__getResponse):
        inst = NewsScraper.getInstance('http://127.0.0.1')
        mock__getResponse.return_value = b' <a id="x">1</a><A id="a">2</a><b id="b">3</a><b href="foo" id="x">4</a><ac width=100>4</ac>'
        res4 = inst.getArticleList()
        expected_res4 = []
        self.assertEqual(expected_res4, res4)
