
NEPAL_DISTRICTS = [
    # Province 1
    ('bhojpur', 'Bhojpur'), ('dhankuta', 'Dhankuta'), ('ilam', 'Ilam'),
    ('jhapa', 'Jhapa'), ('khotang', 'Khotang'), ('morang', 'Morang'),
    ('okhaldhunga', 'Okhaldhunga'), ('panchthar', 'Panchthar'),
    ('sankhuwasabha', 'Sankhuwasabha'), ('solukhumbu', 'Solukhumbu'),
    ('sunsari', 'Sunsari'), ('taplejung', 'Taplejung'),
    ('terhathum', 'Terhathum'), ('udayapur', 'Udayapur'),
    
    # Province 2
    ('bara', 'Bara'), ('dhanusa', 'Dhanusa'), ('mahottari', 'Mahottari'),
    ('parsa', 'Parsa'), ('rautahat', 'Rautahat'), ('saptari', 'Saptari'),
    ('sarlahi', 'Sarlahi'), ('siraha', 'Siraha'),
    
    # Bagmati
    ('bhaktapur', 'Bhaktapur'), ('chitwan', 'Chitwan'),
    ('dhading', 'Dhading'), ('dolakha', 'Dolakha'),
    ('kathmandu', 'Kathmandu'), ('kavrepalanchok', 'Kavrepalanchok'),
    ('lalitpur', 'Lalitpur'), ('makwanpur', 'Makwanpur'),
    ('nuwakot', 'Nuwakot'), ('ramechhap', 'Ramechhap'),
    ('rasuwa', 'Rasuwa'), ('sindhuli', 'Sindhuli'),
    ('sindhupalchok', 'Sindhupalchok'),
    
    # Gandaki
    ('baglung', 'Baglung'), ('gorkha', 'Gorkha'), ('kaski', 'Kaski'),
    ('lamjung', 'Lamjung'), ('manang', 'Manang'), ('mustang', 'Mustang'),
    ('myagdi', 'Myagdi'), ('nawalpur', 'Nawalpur'), ('parbat', 'Parbat'),
    ('syangja', 'Syangja'), ('tanahu', 'Tanahu'),
    
    # Lumbini
    ('arghakhanchi', 'Arghakhanchi'), ('banke', 'Banke'), ('bardiya', 'Bardiya'),
    ('dang', 'Dang'), ('gulmi', 'Gulmi'), ('kapilvastu', 'Kapilvastu'),
    ('parasi', 'Parasi'), ('palpa', 'Palpa'), ('pyuthan', 'Pyuthan'),
    ('rolpa', 'Rolpa'), ('rukum_east', 'Rukum East'), ('rupandehi', 'Rupandehi'),
    
    # Karnali
    ('dailekh', 'Dailekh'), ('dolpa', 'Dolpa'), ('humla', 'Humla'),
    ('jajarkot', 'Jajarkot'), ('jumla', 'Jumla'), ('kalikot', 'Kalikot'),
    ('mugu', 'Mugu'), ('salyan', 'Salyan'), ('surkhet', 'Surkhet'),
    ('rukum_west', 'Rukum West'),
    
    # Sudurpashchim
    ('achham', 'Achham'), ('baitadi', 'Baitadi'), ('bajhang', 'Bajhang'),
    ('bajura', 'Bajura'), ('dadeldhura', 'Dadeldhura'), ('darchula', 'Darchula'),
    ('doti', 'Doti'), ('kailali', 'Kailali'), ('kanchanpur', 'Kanchanpur'),
]

# Sort alphabetically for better UX
NEPAL_DISTRICTS = sorted(NEPAL_DISTRICTS, key=lambda x: x[1])

# Business types for buyers
BUSINESS_TYPES = [
    ('RESTAURANT', 'Restaurant'),
    ('RETAILER', 'Retailer'),
    ('WHOLESALER', 'Wholesaler'),
    ('HOTEL', 'Hotel'),
    ('CATERING', 'Catering Service'),
    ('PROCESSOR', 'Food Processor'),
]