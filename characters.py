"""
characters = {
    "Pecorine" : {
        "Pecorine (Summer)" : 1,
        "Pecorine (Princess)" : 1,
        "Pecorine (New Year)" : 1,
        "Pecorine (Overload)" : 1,
    },
    "Kokkoro" : {
        "Kokkoro (Summer)" : 1,
        "Kokkoro (New Year)" : 1,
        "Kokkoro (Princess)" : 1,
        "Kokkoro (Ritual Garment)" : 1,
        "Kokkoro (Ranger)" : 1,
    },
    "Kyaru" : {
        "Kyaru (Summer)" : 1,
        "Kyaru (New Year)" : 1,
        "Kyaru (Princess)" : 1,
        "Kyaru (Overload)" : 1,
    },
    "Shefi" : {
        "Shefi (New Year)" : 1,
    },
    "Yui" : {
        "Yui (New Year)" : 1,  
        "Yui (Princess)" : 1,
        "Yui (Ritual Garment)" : 1,
        "Yui (Summer)" : 1,
    },
    "Rei" : {
        "Rei (New Year)" : 1,
        "Rei (Halloween)" : 1,
        "Rei (Princess)" : 1,
        "Rei (Summer)" : 1,
    },
    "Hiyori" : {
        "Hiyori (New Year)" : 1,
        "Hiyori (Princess)" : 1,
        "Hiyori (Summer)" : 1,
    },
    "Shizuru" : {
        "Shizuru (Valentine)" : 1,
        "Shizuru (Summer)" : 1,
        "Shizuru (Noir)" : 1,
    },
    "Rino" : {
        "Rino (Wonder)" : 1,
        "Rino (Christmas)" : 1,
    },
    "Labyrista" : {
        "Labyrista (Overload)" : 1,
    },
    "Nozomi" : {
        "Nozomi (Christmas)" : 1,
        "Nozomi (Summer)" : 1,
        "Nozomi (Liberator)" : 1,
    },
    "Chika" : {
        "Chika (Christmas)" : 1,
        "Chika (Summer)" : 1,
    },
    "Tsumugi" : {
        "Tsumugi (Halloween)" : 1,
        "Tsumugi (Summer)" : 1,
    },
    "Misogi" : {
        "Misogi (Halloween)" : 1,
        "Misogi (Summer)" : 1,
    },
    "Mimi" : {
        "Mimi (Halloween)" : 1,
        "Mimi (Summer)" : 1,
    },
    "Kyouka" : {
        "Kyouka (Halloween)" : 1,
        "Kyouka (Summer)" : 1,
    },
    "Misato" : {
        "Misato (Summer)" : 1,
        "Misato (New Year)" : 1,
    },
    "Aoi" : {
        "Aoi (Transfer Student)" : 1,
        "Aoi (Workwear)" : 1,
        "Aoi (Camp)" : 1,
    },
    "Hatsune" : {
        "Hatsune (Summer)" : 1,
    },
    "Ilya" : {
        "Ilya (Christmas)" : 1,
    },
    "Akari" : {
        "Akari (Angel)" : 1,
        "Akari (Christmas)" : 1,
    },
    "Yori" : {
        "Yori (Angel)" : 1,
        "Yori (Christmas)" : 1,
    },
    "Shinobu" : {
        "Shinobu (Halloween)" : 1,
        "Shinobu (Pirate)" : 1,
    },
    "Miyako" : {
        "Miyako (Halloween)" : 1,
        "Miyako (Christmas)" : 1,
    },
    "Jun" : {
        "Jun (Summer)" : 1,
        "Jun (Christmas)" : 1,
    },
    "Tomo" : {
        "Tomo (Magical)" : 1,
        "Tomo (Halloween)" : 1,
    },
    "Christina" : {
        "Christina (Christmas)" : 1,
        "Christina (Wild)" : 1,
    },
    "Matsuri" : {
        "Matsuri (Halloween)" : 1,
        "Matsuri (Wild)" : 1,
    },
    "Saren" : {
        "Saren (Summer)" : 1,
        "Saren (Christmas)" : 1,
    },
    "Suzume" : {
        "Suzume (Summer)" : 1,
        "Suzume (New Year)" : 1,
    },
    "Kurumi" : {
        "Kurumi (Christmas)" : 1,
        "Kurumi (Stage)" : 1,
    },
    "Ayane" : {
        "Ayane (Christmas)" : 1,
        "Ayane (Explorer)" : 1,
    },
    "Maho" : {
        "Maho (Summer)" : 1,
        "Maho (Cinderella)" : 1,
        "Maho (Explorer)" : 1,
    },
    "Makoto" : {
        "Makoto (Summer)" : 1,
        "Makoto (Cinderella)" : 1,
    },
    "Kaori" : {
        "Kaori (Summer)" : 1,
        "Kaori (Halloween)" : 1,
    },
    "Kasumi" : {
        "Kasumi (Magical)" : 1,
        "Kasumi (Summer)" : 1,
    },
    "Mahiru" : {
        "Mahiru (Ranger)" : 1,
        "Mahiru (Christmas)" : 1,
    },
    "Rima" : {
        "Rima (Cinderella)" : 1,
    },
    "Shiori" : {
        "Shiori (Magical)" : 1,
        "Shiori (Ranger)" : 1,
    },
    "Rin" : {
        "Rin (Ranger)" : 1,
        "Rin (Halloween)" : 1,
    },
    "Akino" : {
        "Akino (Christmas)" : 1,
    },
    "Tamaki" : {
        "Tamaki (Summer)" : 1,
        "Tamaki (Workwear)" : 1,
        "Tamaki (Cafe)" : 1,
    },
    "Mifuyu" : {
        "Mifuyu (Summer)" : 1,
        "Mifuyu (Workwear)" : 1,
    },
    "Yukari" : {
        "Yukari (Christmas)" : 1,
        "Yukari (Camp)" : 1,
    },
    "Nanaka" : {
        "Nanaka (Summer)" : 1,
        "Nanaka (Halloween)" : 1,
    },
    "Anna" : {
        "Anna (Summer)"  : 1,
        "Anna (Pirate)" : 1,
    },
    "Ruka" : {
        "Ruka (Summer)"  : 1,
        "Ruka (New Year)"  : 1,
    },
    "Eriko" : {
        "Eriko (Valentine)"  : 1,
        "Eriko (Summer)" : 1,
    },
    "Mitsuki" : {
        "Mitsuki (Ooedo)" : 1,
        "Mitsuki (New Year)" : 1,
    },
    "Io" : {
        "Io (Summer)" : 1,
        "Io (Noir)" : 1,
    },
    "Misaki" : {
        "Misaki (Halloween)" : 1,
        "Misaki (Stage)" : 1,
    },
    "Suzuna" : {
        "Suzuna (Summer)" : 1,
        "Suzuna (Halloween)" : 1,
    },
    "Monika" : {
        "Monika (Magical)" : 1,
        "Monika (Cafe)" : 1,
    },
    "Kuuka" : {
        "Kuuka (Ooedo)" : 1,
        "Kuuka (Noir)" : 1,
    },
    "Ayumi" : {
        "Ayumi (Wonder)" : 1,
        "Ayumi (Phantom Thief)" : 1,
    },
    "Ninon" : {
        "Ninon (Ooedo)" : 1,
        "Ninon (Halloween)" : 1,
    },
    "Yuki" : {
        "Yuki (Ooedo)" : 1,
    },
    "Chloe" : {
        "Chloe (School Festival)" : 1,
    },
    "Yuni" : {
        "Yuni (School Festival)" : 1,
    },
    "Chieru" : {
        "Chieru (School Festival)" : 1,
    },
    "Kaya" : {
        "Kaya (Time Travel)" : 1,
        "Kaya (Liberator)" : 1,
    },
    "Inori" : {
        "Inori (Time Travel)" : 1,
        "Inori (Phantom Thief)" : 1,
    },
    "Homare" : {
        "Homare (New Year)" : 1,
    },
    "Creditta" : {

    },
    "Ranpha" : {

    },
    "Nea" : {

    },
    "Misora" : {

    },
    "Riri (Fallen)" : {

    },
    "Djeeta" : {
        "Djeeta (Warlock)" : 1,
    },
    "Vikala":{

    },
    "Arisa" : {

    },
    "Luna" : {

    },
    "Anne" : {

    },
    "Grea" : {

    },
    "Lou" : {

    },
    "Vampy" : {

    },
    "Muimi" : {
        "Muimi (New Year)" : 1,
        "Muimi (Liberator)" : 1,
    },
    "Neneka" : {
        "Neneka (New Year)" : 1,
    },
    "Karin" : {
        "Karin (Alchemist)" : 1,
    },
    "Kaiser Insight" : {

    },
    "Ameth" : {

    },
    "Hatsune & Shiori" : {

    },
    "Misogi & Mimi & Kyouka" : {

    },
    "Akino & Saren" : {

    },
    "Anne & Grea" : {

    },
    "Emilia" : {

    },
    "Rem" : {

    },
    "Ram" : {

    },
    "Uzuki (Deremasu)" : {

    },
    "Mio (Deremasu)": {

    },
    "Rin (Deremasu)" : {

    },
}
"""

characters = {
    "Pecorine" : 1,
    "Pecorine (Summer)" : 1,
    "Pecorine (Princess)" : 1,
    "Pecorine (New Year)" : 1,
    "Pecorine (Overload)" : 1,
    "Kokkoro" : 1,
    "Kokkoro (Summer)" : 1,
    "Kokkoro (New Year)" : 1,
    "Kokkoro (Princess)" : 1,
    "Kokkoro (Ritual Garment)" : 1,
    "Kokkoro (Ranger)" : 1,
    "Kyaru" : 1,
    "Kyaru (Summer)" : 1,
    "Kyaru (New Year)" : 1,
    "Kyaru (Princess)" : 1,
    "Kyaru (Overload)" : 1,
    "Shefi" : 1,
    "Shefi (New Year)" : 1,
    "Yui" : 1,
    "Yui (New Year)" : 1,  
    "Yui (Princess)" : 1,
    "Yui (Ritual Garment)" : 1,
    "Yui (Summer)" : 1,
    "Rei" : 1,
    "Rei (New Year)" : 1,
    "Rei (Halloween)" : 1,
    "Rei (Princess)" : 1,
    "Rei (Summer)" : 1,
    "Hiyori" : 1,
    "Hiyori (New Year)" : 1,
    "Hiyori (Princess)" : 1,
    "Hiyori (Summer)" : 1,
    "Shizuru" : 1,
    "Shizuru (Valentine)" : 1,
    "Shizuru (Summer)" : 1,
    "Shizuru (Noir)" : 1,
    "Rino" : 1,
    "Rino (Wonder)" : 1,
    "Rino (Christmas)" : 1,
    "Labyrista" : 1,
    "Labyrista (Overload)" : 1,
    "Nozomi" : 1,
    "Nozomi (Christmas)" : 1,
    "Nozomi (Summer)" : 1,
    "Nozomi (Liberator)" : 1,
    "Chika" : 1,
    "Chika (Christmas)" : 1,
    "Chika (Summer)" : 1,
    "Tsumugi" : 1,
    "Tsumugi (Halloween)" : 1,
    "Tsumugi (Summer)" : 1,
    "Misogi" : 1,
    "Misogi (Halloween)" : 1,
    "Misogi (Summer)" : 1,
    "Mimi" : 1,
    "Mimi (Halloween)" : 1,
    "Mimi (Summer)" : 1,
    "Kyouka" : 1,
    "Kyouka (Halloween)" : 1,
    "Kyouka (Summer)" : 1,
    "Misato" : 1,
    "Misato (Summer)" : 1,
    "Misato (New Year)" : 1,
    "Aoi" : 1,
    "Aoi (Transfer Student)" : 1,
    "Aoi (Workwear)" : 1,
    "Aoi (Camp)" : 1,
    "Hatsune" : 1,
    "Hatsune (Summer)" : 1,
    "Ilya" : 1,
    "Ilya (Christmas)" : 1,
    "Akari" : 1,
    "Akari (Angel)" : 1,
    "Akari (Christmas)" : 1,
    "Yori" : 1,
    "Yori (Angel)" : 1,
    "Yori (Christmas)" : 1,
    "Shinobu" : 1,
    "Shinobu (Halloween)" : 1,
    "Shinobu (Pirate)" : 1,
    "Miyako" : 1,
    "Miyako (Halloween)" : 1,
    "Miyako (Christmas)" : 1,
    "Jun" : 1,
    "Jun (Summer)" : 1,
    "Jun (Christmas)" : 1,
    "Tomo" : 1,
    "Tomo (Magical)" : 1,
    "Tomo (Halloween)" : 1,
    "Christina" : 1,
    "Christina (Christmas)" : 1,
    "Christina (Wild)" : 1,
    "Matsuri" : 1,
    "Matsuri (Halloween)" : 1,
    "Matsuri (Wild)" : 1,
    "Saren" : 1,
    "Saren (Summer)" : 1,
    "Saren (Christmas)" : 1,
    "Suzume" : 1,
    "Suzume (Summer)" : 1,
    "Suzume (New Year)" : 1,
    "Kurumi" : 1,
    "Kurumi (Christmas)" : 1,
    "Kurumi (Stage)" : 1,
    "Ayane" : 1,
    "Ayane (Christmas)" : 1,
    "Ayane (Explorer)" : 1,
    "Maho" : 1,
    "Maho (Summer)" : 1,
    "Maho (Cinderella)" : 1,
    "Maho (Explorer)" : 1,
    "Makoto" : 1,
    "Makoto (Summer)" : 1,
    "Makoto (Cinderella)" : 1,
    "Kaori" : 1,
    "Kaori (Summer)" : 1,
    "Kaori (Halloween)" : 1,
    "Kasumi" : 1,
    "Kasumi (Magical)" : 1,
    "Kasumi (Summer)" : 1,
    "Mahiru" : 1,
    "Mahiru (Ranger)" : 1,
    "Mahiru (Christmas)" : 1,
    "Rima" : 1,
    "Rima (Cinderella)" : 1,
    "Shiori" : 1,
    "Shiori (Magical)" : 1,
    "Shiori (Ranger)" : 1,
    "Rin" : 1,
    "Rin (Ranger)" : 1,
    "Rin (Halloween)" : 1,
    "Akino" : 1,
    "Akino (Christmas)" : 1,
    "Tamaki" : 1,
    "Tamaki (Summer)" : 1,
    "Tamaki (Workwear)" : 1,
    "Tamaki (Cafe)" : 1,
    "Mifuyu" : 1,
    "Mifuyu (Summer)" : 1,
    "Mifuyu (Workwear)" : 1,
    "Yukari" : 1,
    "Yukari (Christmas)" : 1,
    "Yukari (Camp)" : 1,
    "Nanaka" : 1,
    "Nanaka (Summer)" : 1,
    "Nanaka (Halloween)" : 1,
    "Anna" : 1,
    "Anna (Summer)"  : 1,
    "Anna (Pirate)" : 1,
    "Ruka" : 1,
    "Ruka (Summer)"  : 1,
    "Ruka (New Year)"  : 1,
    "Eriko" : 1,
    "Eriko (Valentine)"  : 1,
    "Eriko (Summer)" : 1,
    "Mitsuki" : 1,
    "Mitsuki (Ooedo)" : 1,
    "Mitsuki (New Year)" : 1,
    "Io" : 1,
    "Io (Summer)" : 1,
    "Io (Noir)" : 1,
    "Misaki" : 1,
    "Misaki (Halloween)" : 1,
    "Misaki (Stage)" : 1,
    "Suzuna" : 1,
    "Suzuna (Summer)" : 1,
    "Suzuna (Halloween)" : 1,
    "Monika" : 1,
    "Monika (Magical)" : 1,
    "Monika (Cafe)" : 1,
    "Kuuka" : 1,
    "Kuuka (Ooedo)" : 1,
    "Kuuka (Noir)" : 1,
    "Ayumi" : 1,
    "Ayumi (Wonder)" : 1,
    "Ayumi (Phantom Thief)" : 1,
    "Ninon" : 1,
    "Ninon (Ooedo)" : 1,
    "Ninon (Halloween)" : 1,
    "Yuki" : 1,
    "Yuki (Ooedo)" : 1,
    "Chloe" : 1,
    "Chloe (School Festival)" : 1,
    "Yuni" : 1,
    "Yuni (School Festival)" : 1,
    "Chieru" : 1,
    "Chieru (School Festival)" : 1,
    "Kaya" : 1,
    "Kaya (Time Travel)" : 1,
    "Kaya (Liberator)" : 1,
    "Inori" : 1,
    "Inori (Time Travel)" : 1,
    "Inori (Phantom Thief)" : 1,
    "Homare" : 1,
    "Homare (New Year)" : 1,
    "Creditta" : 1,
    "Ranpha" : 1,
    "Nea" : 1,
    "Misora" : 1,
    "Riri (Fallen)" : 1,
    "Djeeta" : 1,
    "Djeeta (Warlock)" : 1,
    "Vikala": 1,
    "Arisa" : 1,
    "Luna" : 1,
    "Anne" : 1,
    "Grea" : 1,
    "Lou" : 1,
    "Vampy" : 1,
    "Muimi" : 1,
    "Muimi (New Year)" : 1,
    "Muimi (Liberator)" : 1,
    "Neneka" : 1,
    "Neneka (New Year)" : 1,
    "Karin" : 1,
    "Karin (Alchemist)" : 1,
    "Kaiser Insight" : 1,
    "Ameth" : 1,
    "Hatsune & Shiori" : 1,
    "Misogi & Mimi & Kyouka" : 1,
    "Akino & Saren" : 1,
    "Anne & Grea" : 1,
    "Emilia" : 1,
    "Rem" : 1,
    "Ram" : 1,
    "Uzuki (Deremasu)" : 1,
    "Mio (Deremasu)": 1,
    "Rin (Deremasu)" : 1,
}