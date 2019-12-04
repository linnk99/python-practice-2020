class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self._contacts = []
        
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                print('El contacto {} ha sido eliminado'.format(contact.name))
                del self._contacts[idx]
                break
            
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()
            
    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._contacts[idx].name = str(input('Escribe el nombre del contacto: '))
                self._contacts[idx].phone = str(input('Escribe el telefono del contacto: '))
                self._contacts[idx].email = str(input('Escribe el email del contacto: '))
                
                print('El contacto {} ha sido actualizado'.format(contact.name))
            else:
                self._not_found()
                
    
    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')
        
    def _not_found(self):
        print('**********')
        print('No encontrado!!')
        print('**********')
        
def run():
    
    contact_book = ContactBook()
    
    while True:
        command = str(input('''
            Que deseas hacer?
            
            [a]gregar contacto                    
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir            
        '''))
        
        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            
            contact_book.add(name, phone, email)
            
        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto a actualizar: '))
            
            contact_book.update(name)
            
        elif command == 'b':
            name = str(input('Escribe el nombre del contacto a buscar: '))
            
            contact_book.search(name)
            
        elif command == 'e':
            
            name = str(input('Escribe el nombre del contacto: '))
            
            contact_book.delete(name)
            
        elif command == 'l':
            
            contact_book.show_all()
            
        elif command == 's':
            break
        
        else:
            print('Comando no encontrado')
            

if __name__ == "__main__":
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()