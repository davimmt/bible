class Division:
    def OldTestament(self):
        return "Genesis/Gn", "Malaquias/Ml"
    def NewTestament(self):
        return "Mateus/Mt", "Apocalipse/Ap"
    def test(self):
        return "Mateus/Mt", "Marcos/Mc"
    
    def between_two_values(self, dictionary, start, end):
        if end == "":
            end = start

        matches = {}
        start_stop = False
        for book in dictionary:
            if book == start:
                start_stop = True
        
            if start_stop:
                matches[book] = dictionary[book]
            
            if book == end:
                start_stop = False

        return matches