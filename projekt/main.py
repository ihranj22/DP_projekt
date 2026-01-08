from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from gramatika_receptiLexer import gramatika_receptiLexer
from gramatika_receptiParser import gramatika_receptiParser
from gramatika_receptiListener import gramatika_receptiListener


class MyListener(gramatika_receptiListener):
    def __init__(self):
        self.intent = "ERROR"
        self.ingredients = []

    def enterPozdrav(self, ctx):
        self.intent = "POZDRAV"

    def enterPomoc(self, ctx):
        self.intent = "POMOC"

    def enterIzlaz(self, ctx):
        self.intent = "IZLAZ"

    def enterSastojciInput(self, ctx):
        self.intent = "SASTOJCI"

    def enterZahtjevRecept(self, ctx):
        self.intent = "RECEPT"

    def enterListaSastojaka(self, ctx):
        for t in ctx.SASTOJAK():
            self.ingredients.append(t.getText())


def parse_ulaz(text: str) -> MyListener:
    listener = MyListener()

    text = text.lower().strip()

    input_stream = InputStream(text)
    lexer = gramatika_receptiLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = gramatika_receptiParser(tokens)

    tree = parser.ulaz()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener


def help_text() -> str:
    return (
        "Možeš napisati:\n"
        "- pozdrav / bok / hej\n"
        "- unos sastojaka: 'imam...' ili 'sastojci:...'\n"
        "- traženje recepta: 'daj recept s' ili 'sto mogu kuhati od'\n"
        "- izlaz: 'izlaz' ili 'dovidenja'\n"
    )


def generate_recipe(ingredients: list[str]) -> str:
    s = set(ingredients)

    if s == {"jaja", "sir", "sol"}:
        return (
            "Kajgana sa sirom\n"
            "1) Razbij jaja u zdjelu i posoli.\n"
            "2) Ulij u zagrijanu tavu i lagano miješaj.\n"
            "3) Pred kraj dodaj sir i pusti da se otopi.\n"
        )
    
    if s == {"jaja", "paprika", "tikvice", "sir", "papar", "ulje"}:
        return (
            "Omlet s povrćem i sirom\n"
            "1) Nasjeckaj povrće i poprži ga na malo ulja 3-4 minute.\n"
            "2) Umuti jaja, dodaj sol i papar, zatim ih prelij preko povrća i pospi naribanim sirom.\n"
            "3) Pokrij i peci 5 minuta na laganoj vatri dok se jaja ne stisnu.\n"
        )
    
    if s == {"grah", "tuna", "luk", "secerac", "ulje", "sol", "papar"}:
        return (
            "Grah salata s tunom, lukom i kukuruzom\n"
            "1) Ocijedi grah, tunu i kukuruz, zatim ih pomiješaj u zdjeli.\n"
            "2) Dodaj sitno nasjeckani luk, ulje, sol i papar.\n"
            "3) Sve dobro promiješaj i posluži hladno ili sobne temperature.\n"
        )

    if s == {"tortilje", "umak od rajcice", "sir", "sunka", "origano"}:
        return (
            "Brza pizza na tortilji\n"
            "1) Zagrij pećnicu na 200°C.\n"
            "2) Namaži tortilju umakom od rajčice, dodaj sir, sunku i origano.\n"
            "3) Peci 7-10 minuta dok sir ne postane zlatan i rastopljen.\n"
        )
    
    if s == {"krumpir", "mlijeko"}:
        return (
            "Pire krumpir\n"
            "1) Oguli i skuhaj krumpir u slanoj vodi.\n"
            "2) Zgnječi krumpir i dodaj malo mlijeka.\n"
            "3) Po želji dodaj maslac.\n"
        )
    
    if s == {"tjestenina", "sir", "maslac"}:
        return (
            "Tjestenina sa sirom\n"
            "1) Skuhaj tjesteninu.\n"
            "2) Dodaj sir i malo maslaca."
        )
    
    if s == {"krumpir", "luk"}:
        return (
            "Restani krumpir\n"
            "1) Skuhaj krumpir.\n"
            "2) Na tavi poprži luk.\n"
            "3) Dodaj krumpir i zapeci."
        )
    

    if s == {"piletina", "riza", "ulje"} :
        return (
            "Piletina s rižom\n"
            "1) Preprži piletinu na malo ulja.\n"
            "2) Dodaj rižu i podlij vodom/temeljcem.\n"
            "3) Kuhaj dok riža ne omekša.\n"
        )
    
    if s == {"kvasac", "secer", "mlijeko", "brasno", "sol", "ulje", "jaja", "margarin"} :
        return (
            "Brzi kroasani\n"
            "1) Kvasac pomiješajte s malo mlijeka i šećera te ostavite na toplom mjestu da se digne.\n"
            "2) U brašno dodajte ulje, jaje, žumance, sol, promiješajte pa dodajte dignuti kvasac. Nakon toga dodajte toplo mlijeko, izradite glatko tijesto i stavite ga na toplo mjesto da se diže.\n"
            "3) Kada tijesto udvostruči volumen, razvaljajte ga na debljinu od 1 cm. Po površini tijesta naribajte margarin, a zatim ga savijte u roladu. Podijelite je na pet dijelova i ostavite neka se diže oko 20 minuta na toplom mjestu.\n"
            "4) Razvaljajte svaku roladu, izrežite manje trokute te ih zamotajte u obliku kiflica (kroasana).\n"
            "5) Od jedne rolade možete dobiti oko 8 kroasana.\n"
            "3) Premažite ih razmućenim jajetom i pecite u zagrijanoj pećnici na 200°C oko 15 minuta..\n"
        )
    
    if s == {"mljeveno meso", "brasno", "luk", "parmezan", "prsut", "vegeta", "cesnjak", "krusne mrvice", "ulje"} :
        return (
            "Mesne okruglice u umaku\n"
            "1) Mljevenom mesu dodajte jaje, krušne mrvice, nasjeckani češnjak, Vegetu, pršut narezan na kockice, naribani parmezan, nasjeckani luk i naribani muškatni oraščić. Smjesu dobro izmiješajte i oblikujte male kuglice.\n"
            "2) Uvaljajte ih lagano u brašno i pecite u zagrijanom ulju oko 8 minuta. Izvadite ih na kuhinjski papir kako bi se upila suvišna masnoća.\n"
            "3) Zagrijte ljutu salsu u koju ste dodali vode, stavite okruglice i još kratko prokuhajte.\n"
        )
    
    if s == {"brasno", "maslac", "sol", "kvasac", "voda"} :
        return (
            "Domaći kruh\n"
            "1) Kvasac razmrvite, dodajte malo šećera i 50 ml mlake vode pa ostavite na toplom mjestu oko 10 minuta.\n"
            "2) Prosijanom brašnu dodajte sol i kvasac pa pomiješajte s preostalom vodom.\n"
            "3) Umiješajte rastopljeni maslac i zamijesite glatko tijesto. Ostavite neka se diže na toplom mjestu oko 30 minuta.\n"
            "4) Tijesto premijesite, oblikujte štrucu i stavite u namašćeni kalup. Prije pečenja tijesto stavite još jedanput dizati.\n"
            "5) Zarežite ga nožem i poprskajte vodom, stavite u zagrijanu pećnicu na 225°C i pecite oko 10 minuta, a zatim smanjite na 170°C i pecite još 35 minuta.\n"
        )
    
    if s == {"hrenovke", "riza", "secerac", "paprika", "luk", "sol"} :
        return (
            "Salata s hrenovkama\n"
            "1) Hrenovke kratko prokuhajte, ohladite i narežite na kolutiće.\n"
            "2) Rižu skuhajte u blago posoljenoj vodi.\n"
            "3) Ohlađenoj riži dodajte hrenovke, kukuruz šećerac, papriku narezanu na kockice i luk narezan na kolutiće. Sve dobro izmiješajte i dobro ohladite.\n"
        )
    
    if s == {"piletina", "limun", "umak od soje", "vegeta", "ulje", "brasno", "jaja", "sol", "papar", "krusne mrvice", "sezam"}  :
        return (
            "Piletina sa sezamom\n"
            "1) Piletinu narežite na krupnije trake. Pokapajte ih limunovim sokom i umakom od soje te pospite Vegetom. Ostavite da malo odstoje.\n"
            "2) Jaja razmutite , posolite i dodajte malo crnog papara. Komad po komad piletine uvaljajte u brašno, zatim umočite u pripremljena jaja, a na kraju ih uvaljajte u mješavinu i krušnih mrvica i sezama.\n"
            "3) Stavite ih pržiti u duboko vruće ulje, na srednju temperaturu, dok ne poprime zlatnožutu boju.\n"
            "4) Izvadite ih na upijajući papir.\n"
        )
    
    if s == {"tuna", "jaja", "maslac", "kiselo vrhnje", "luk", "senf", "masline"}  :
        return (
            "Namaz od tune\n"
            "1) Maslac pjenasto izmiješajte, a tvrdo kuhano jaje i tunjevinu sitno nasjeckajte ili sameljite.\n"
            "2) JU maslac umiješajte pripremljeni luk, jaje i tunu.\n"
            "3) Dodajte vrhnje, senf i masline. Sve dobro izmiješajte i ohladite.\n"
        )
    
    if s == {"brasno", "mlijeko", "jaja", "sunka", "sir", "persin", "ulje", "sol", "krusne mrvice", "krusne mrvice"}  :
        return (
            "Popečci sa šunkom\n"
            "1) Brašno umiješajte u mlijeko i miješajući zagrijavajte na laganoj vatri dok ne dobijete gustu masu.\n"
            "2) Maknite s vatre, malo ohladite, dodajte jaje, sitno narezanu šunku, naribani sir i peršin, pa sve dobro promiješajte.\n"
            "3) Pripremljenu smjesu ohladite, rukama oblikujte popečke, uvaljajte ih u brašno, zatim u razrađena posoljena jaja i na kraju u krušne mrvice.\n"
            "4) Pržite u zagrijanom ulju do zlatnožute boje.\n"
        )
    
    if s == {"riza", "kupus", "paprika", "luk", "mrkva", "dumbir", "sezam", "ulje", "umak od soje", "sol", "papar", "jaja"} :
        return (
            "Pržena riža s jajem na oko\n"
            "1) Rižu isperite hladnom vodom i skuhajte prema uputama na pakiranju.\n"
            "2) Povrće pripremite: kupus i papriku narežite na tanke rezance, luk na polumjesece, mrkvu na trakice, mladi luk na kolutiće, a đumbir sitno naribajte.\n"
            "3) Sezamove sjemenke kratko tostirajte na suhoj tavi, neprestano miješajući kako ne bi zagorjele.\n"
            "3) Kuhaj dok riža ne omekša.\n"
            "4) U dobro zagrijan wok dodajte ulje, zatim ubacite luk, papriku i mrkvu. Pržite uz miješanje 2 minute.\n"
            "5) Dodajte kupus i đumbir, nastavite miješati još minutu. Posolite, popaprite i dodajte soja sos.\n"
            "6) Umiješajte kuhanu rižu i nastavite pržiti dok se zrna ne počnu odvajati jedno od drugog. Sve dobro izmiješajte.\n"
            "7) U drugoj tavi ili woku ispecite jaja na oko.\n"
            "8) Na tanjur servirajte rižu s povrćem, na vrh stavite pečeno jaje, a sve pospite tostiranim sezamom i mladim lukom.\n"
        )
    
    if s == {"brasno", "kvasac", "secer", "sol", "sezam", "mlijeko", "maslac", "svjezi sir", "sir", "kiselo vrhnje", "jaja", "persin"}  :
        return (
            "Torbice sa sirom\n"
            "1) Kvasac razmrvite u 50 ml mlakog mlijeka, dodajte šećer i ostavite neka stoji na toplom mjestu dok se kvasac ne zapjeni (6-7 minuta).\n"
            "2) U dublju zdjelu stavite brašno, dodajte sol, sezam, žumanca, otopljeni maslac i kvasac, pa dolijevanjem mlijeka umijesite glatko tijesto. Ostavite ga neka se diže na toplom mijestu dok ne udvostruči volumen.\n"
            "3) U međuvremenu pripremite nadjev. Svježi kravlji sir dobro ocijedite, dodajte naribani edamer, kiselo vrhnje, jaje, brašno i peršin, pa sve dobro promiješajte.\n"
            "4) Tijesto razvaljajte na pobrašnjenoj površini na oko 1 cm. Izrežite ga na kvadrate dimenzija 6×6 cm, a u sredinu svakog kvadrata stavite 1-2 žličice nadjeva.\n"
            "5) Rubove kvadrata premažite razmućenim jajetom, pa oblikujte zavežljaje. Zavežljaje stavite na namašćeni lim i ostavite neka se dižu još 15 minuta.\n"
            "6) Premažite ih preostalim razmućenim jajetom, po želji dodatno pospite sezamom (1-2 žlice) i pecite u pećnici zagrijanoj na 180°C 25 minuta.\n"
        )
    
    if s == {"tortilje", "piletina", "paprika", "zelena salata", "majoneza", "sol", "papar", "ulje"} :
        return (
            "Tortilja s piletinom i povrćem\n"
            "1) Piletinu ispeci na naglo na tavi s malo ulja.\n"
            "2) Kad je pečena, nareži nju i povrće na tanke trakice.\n"
            "3) Namaži tortilju majonezom, zatim rasporedi piletinu i povrće.\n"
            "4) Smotaj i uživaj!\n"
        )
    
    if s == {"riza", "tuna", "luk", "vrhnje za kuhanje", "sol", "papar", "persin"} :
        return (
            "Rižoto od tune\n"
            "1) Skuhaj rižu prema uputama ili koristi već skuhanu rižu.\n"
            "2) Na tavi poprži sitno nasjeckani luk, dodaj tunu i vrhnje te začini po želji.\n"
            "3) Umiješaj rižu u umak, promiješaj i posluži toplo.\n"
        )
    
    if s == {"grah", "avokado", "secerac", "cesnjak", "sol", "papar", "ulje"} :
        return (
            "Zapečeni grah s avokadom i kukuruzom\n"
            "1) Na malo ulja poprži nasjeckani češnjak i dodaj ocijeđeni grah i kukuruz.\n"
            "2) Kratko zagrij i začini po želji.\n"
            "3) Serviraj s narezanim avokadom na vrhu.\n"
        )
    
    return "Nemam recept za tu kombinaciju. Probaj druge sastojke ili upiši 'pomoc'."


def main():
    print("Chatbot za recepte - upisi 'pomoc' za upute).")
    stored: list[str] = []

    while True:
        user = input("> ").strip()
        if not user:
            continue

        listener = parse_ulaz(user)

        if listener.intent == "POZDRAV":
            print("Pozdrav! Što kuhamo danas? Unesi sastojke.")

        elif listener.intent == "POMOC":
            print(help_text())

        elif listener.intent == "SASTOJCI":
            stored = listener.ingredients
            print(f"Super, zapamtio sam sastojke: {', '.join(stored)}")
            print("Sad napiši 'Daj recept.' ili 'Sto mogu kuhati.'.")

        elif listener.intent == "RECEPT":
            use = listener.ingredients if listener.ingredients else stored
            if not use:
                print("Prvo unesi sastojke.")
            else:
                print(generate_recipe(use))

        elif listener.intent == "IZLAZ":
            print("Doviđenja")
            break

        else:
            print("Nisam razumio. Probaj 'pomoc'.")


if __name__ == "__main__":
    main()
