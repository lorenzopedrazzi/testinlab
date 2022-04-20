class id:
    numero_documento = 0
    def __init__(self, nome, cognome, annorilascio = 2022, annonascita, numero_documento):
        self.nome = nome
        self.cognome = cognome
        self.annorilascio = annorilascio
        self.annonascita = 0
        id.numero_documento += 1
        self.numero_documento = numero_documento


    def set_birth_year(self, anno_nascita):
        if anno_nascita > self.annorilascio:
            self.annonascita = anno_nascita
        else:
            self.annonascita = self.annorilascio

    def get_year(self):
        print(self.annonascita)

    def get_name(self):
        print(self.nome)

    def get_surname(self):
        print(self.cognome)

    def get_year_release(self):
        print(self.annorilascio)

    def get_number_document(self):
        print(self.numero_documento)

