-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2025. Jan 22. 11:27
-- Kiszolgáló verziója: 10.4.27-MariaDB
-- PHP verzió: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `coachify_trainers`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `trainers`
--

CREATE TABLE `trainers` (
  `id` int(11) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `specialization` varchar(255) DEFAULT NULL,
  `available_training_types` varchar(255) DEFAULT NULL,
  `price_range` varchar(255) DEFAULT NULL,
  `languages` varchar(255) DEFAULT NULL,
  `reviews` text DEFAULT NULL,
  `introduction` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- A tábla adatainak kiíratása `trainers`
--

INSERT INTO `trainers` (`id`, `full_name`, `email`, `password`, `location`, `specialization`, `available_training_types`, `price_range`, `languages`, `reviews`, `introduction`) VALUES
(1, 'John Doe', 'johndoe@example.com', 'johndoe123', 'Budapest, Hungary', 'Fogyás', 'Személyes', '5000 HUF/óra', 'Magyar, Angol', 'Nagyon jól segít a céljaim elérésében!', 'A célom, hogy segítsek másoknak a fogyásban és az egészséges életmód kialakításában.'),
(2, 'Jane Smith', 'janesmith@example.com', 'janesmith123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '6000 HUF/óra', 'Magyar, Angol, Német', 'Kitűnő edző, a rehabilitáció során rengeteget segített!', 'A rehabilitáció és a prevenció a szakterületem, hiszek a mozgás gyógyító erejében.'),
(3, 'Mark Johnson', 'markjohnson@example.com', 'markjohnson123', 'Online', 'Erőnléti edzés', 'Személyes', '4000 HUF/óra', 'Angol', 'Nagyon motiváló edző, aki segít fejleszteni az erőnlétemet.', 'Erőnléti edzéseim során a személyre szabott programok és folyamatos visszajelzés a kulcs.'),
(4, 'Laura White', 'laurawhite@example.com', 'laurawhite123', 'Pécs, Hungary', 'Fogyás, Erőnléti edzés', 'Személyes', '5500 HUF/óra', 'Magyar, Angol', 'Segített elérni a fitness céljaimat, miközben megőríztem a motivációmat.', 'Kombinálom az erőnléti és fogyási edzéseket, hogy mindenki elérje az optimális eredményt.'),
(5, 'Robert Brown', 'robertbrown@example.com', 'robertbrown123', 'Székesfehérvár, Hungary', 'Rehabilitáció, Erőnléti edzés', 'Személyes', '7000 HUF/óra', 'Magyar, Angol', 'Professzionális, segítőkész edző, minden edzés után fejlődtem.', 'Rehabilitációs szakemberként az a célom, hogy visszavezesselek a legjobb formádba.'),
(6, 'Emily Clark', 'emilyclark@example.com', 'emilyclark123', 'Budapest, Hungary', 'Fogyás', 'Személyes', '4500 HUF/óra', 'Magyar, Angol, Német', 'Nagyon hasznos tanácsokat kaptam a táplálkozásom javítására.', 'A személyre szabott fogyásprogramok mellett segítek a helyes étrend kialakításában.'),
(7, 'David Lee', 'davidlee@example.com', 'davidlee123', 'Online', 'Erőnléti edzés', 'Személyes', '4800 HUF/óra', 'Angol', 'Erősebb lettem és sokkal jobban érzem magam.', 'Az erőnléti edzésben az alapok és a progresszió elengedhetetlenek, de mindig figyelek a megfelelő technikára.'),
(8, 'Sophia Miller', 'sophiamiller@example.com', 'sophiamiller123', 'Győr, Hungary', 'Rehabilitáció', 'Személyes', '6200 HUF/óra', 'Magyar, Angol', 'A rehabilitációs gyakorlatok során biztos kezekben voltam.', 'Minden esetben a sérülések utáni rehabilitációra koncentrálok, hogy biztonságosan térj vissza a mozgásba.'),
(9, 'Daniel Harris', 'danielharris@example.com', 'danielharris123', 'Online', 'Erőnléti edzés', 'Személyes', '5000 HUF/óra', 'Angol', 'Nagyon jó programot ajánlott, amit könnyen be tudtam illeszteni a napi rutinomba.', 'Az edzéseimet online tartom, ahol a közvetlen visszajelzés és a személyre szabott terv a kulcs a fejlődéshez.'),
(10, 'Olivia Martinez', 'oliviamartinez@example.com', 'oliviamartinez123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '4700 HUF/óra', 'Magyar, Angol', 'Minden edzés nagyon motiváló, és mindig a maximumot hozom ki magamból.', 'A fogyás és a zsírégetés elérése érdekében intenzív edzéseket biztosítok a legjobb eredményekért.'),
(11, 'James Wilson', 'jameswilson@example.com', 'jameswilson123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '5300 HUF/óra', 'Magyar, Angol', 'Egyéni szükségleteimhez igazított rehabilitációs tervet kaptam.', 'A rehabilitációs programok során mindig figyelek a testem jeleire, hogy a legjobban fejlődhessenek.'),
(12, 'Ava Davis', 'avdavis@example.com', 'avdavis123', 'Online', 'Fogyás', 'Személyes', '4900 HUF/óra', 'Magyar, Angol, Olasz', 'Segít a zsírégetésben és a mozgás örömében.', 'Személyre szabott programot biztosítok, hogy mindenkinek a legjobb eredményt nyújtsam a fogyás terén.'),
(13, 'Michael Robinson', 'michaelrobinson@example.com', 'michaelrobinson123', 'Szeged, Hungary', 'Erőnléti edzés', 'Személyes', '5800 HUF/óra', 'Magyar, Angol', 'Nagyon jól érthető edzésprogramot készített számomra.', 'Az erőnléti edzésben a célom, hogy mindenki maximalizálja saját teljesítményét.'),
(14, 'Anna Walker', 'annawalker@example.com', 'annawalker123', 'Budapest, Hungary', 'Rehabilitáció', 'Személyes', '6000 HUF/óra', 'Magyar, Angol', 'Sokat segített a mozgáskorlátozottságom leküzdésében.', 'Sérülések utáni rehabilitációra specializálódtam, hogy mindenki teljesen visszanyerje mozgékonyságát.'),
(15, 'Ethan Lee', 'ethanlee@example.com', 'ethanlee123', 'Online', 'Erőnléti edzés', 'Személyes', '5500 HUF/óra', 'Magyar, Angol', 'Az edzések után gyorsan láttam az eredményeket.', 'A célom, hogy minden egyes edzés során előrelépjünk és a fejlődés folyamatos legyen.'),
(16, 'Zoltán Varga', 'zvarga@example.com', 'zvarga123', 'Budapest, Hungary', 'Súlyzós edzés', 'Személyes', '5500 HUF/óra', 'Magyar', 'Sokat segített abban, hogy helyesen végezzem el az edzéseket!', 'Minden edzésnél a pontos technika és a folyamatos fejlődés a fő célom.'),
(17, 'Gábor Kovács', 'gkovacs@example.com', 'gkovacs123', 'Pécs, Hungary', 'Fogyás', 'Személyes', '5000 HUF/óra', 'Magyar', 'Nagyon jól motivált, hogy elérjem a fitness céljaimat.', 'A mozgás és a táplálkozás harmóniájára helyezem a hangsúlyt a céljaid eléréséhez.'),
(18, 'Eszter Farkas', 'efarkas@example.com', 'efarkas123', 'Székesfehérvár, Hungary', 'Erőnléti edzés', 'Személyes', '6000 HUF/óra', 'Magyar', 'Jó technikai tudással és figyelmes edző.', 'Erőnléti edzésen a célom a stabil alapok megteremtése és a folyamatos fejlődés.'),
(19, 'Katalin Papp', 'kpapp@example.com', 'kpapp123', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '5800 HUF/óra', 'Magyar', 'A rehabilitációs program segített, hogy gyorsan visszatérjek a sporthoz.', 'Szakterületem a rehabilitáció, hogy minél gyorsabban vissza tudd nyerni a mozgékonyságodat.'),
(20, 'László Nagy', 'lnagy@example.com', 'lnagy123', 'Győr, Hungary', 'Súlyzós edzés', 'Személyes', '5900 HUF/óra', 'Magyar', 'Egyedülálló motivációval és edzésprogramokkal.', 'Súlyzós edzéseim során az intenzitás és a helyes végrehajtás kulcsfontosságú.'),
(21, 'Nóra Kiss', 'nkiss@example.com', 'nkiss123', 'Budapest, Hungary', 'Fogyás', 'Személyes', '5200 HUF/óra', 'Magyar', 'Tökéletesen irányított a céljaim felé.', 'A legjobb eredményekhez személyre szabott programokat kínálok, hogy gyorsan elérd a kívánt célt.'),
(22, 'Béla Tóth', 'btoth@example.com', 'btoth123', 'Debrecen, Hungary', 'Erőnléti edzés', 'Személyes', '5400 HUF/óra', 'Magyar', 'Nagyon részletes edzésprogramot kaptam, amivel biztosan fejlődök.', 'Erőnléti edzéseim célja a folyamatos teljesítménynövelés és a megfelelő pihenési idő beállítása.'),
(23, 'Anikó Kovács', 'akovacs@example.com', 'akovacs123', 'Szeged, Hungary', 'Súlyzós edzés', 'Személyes', '5500 HUF/óra', 'Magyar', 'A személyre szabott program segített a fejlődésemben.', 'A súlyzós edzés és a megfelelő étkezés biztosítja az optimális fejlődést minden egyes edző számára.'),
(49, 'Béla Horváth', 'bhorvath@example.com', 'bhorvath123', 'Budapest, Hungary', 'Súlyzós edzés', 'Személyes', '6000 HUF/óra', 'Magyar', 'Nagyon jól segít a formám javításában!', 'Súlyzós edzés közben figyelek a pontos technikai kivitelezésre és a fokozatosságra.'),
(50, 'Péter Varga', 'pvarga@example.com', 'pvarga123', 'Debrecen, Hungary', 'Fogyás', 'Személyes', '5200 HUF/óra', 'Magyar', 'A legjobb edző, segített elérni a céljaimat.', 'Fogyás és zsírégetés, folyamatos fejlődés a legfontosabb számomra.'),
(51, 'Dávid Farkas', 'dfarkas@example.com', 'dfarkas123', 'Pécs, Hungary', 'Rehabilitáció', 'Személyes', '6300 HUF/óra', 'Magyar', 'Minden edzés rendkívül figyelmes és precíz volt.', 'A rehabilitációban a fokozatosságot és a megfelelő pihenőt helyezem előtérbe.'),
(52, 'Zsófia Szabó', 'zszabo@example.com', 'zszabo123', 'Székesfehérvár, Hungary', 'Erőnléti edzés', 'Személyes', '5500 HUF/óra', 'Magyar', 'Nagyon jól motivál, hogy folyamatosan fejlődjek!', 'Edzéseim középpontjában az erőnléti fejlődés és a hatékony munkavégzés áll.'),
(53, 'Tamás Nagy', 'tnagy@example.com', 'tnagy123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '5100 HUF/óra', 'Magyar', 'Rendkívül segítőkész és figyelmes edző.', 'Személyre szabott edzésekkel segítek elérni a fogyási céljaidat.'),
(54, 'Emese Tóth', 'etoth@example.com', 'etoth123', 'Győr, Hungary', 'Erőnléti edzés', 'Személyes', '5600 HUF/óra', 'Magyar', 'Minden edzés kiváló és jól felépített volt.', 'A célom, hogy minden edzés után látványos fejlődést tapasztalj a testépítésben.'),
(55, 'Károly Kiss', 'kkiss@example.com', 'kkiss123', 'Budapest, Hungary', 'Rehabilitáció', 'Személyes', '5800 HUF/óra', 'Magyar', 'Nagyon sokat segített a rehabilitációban, ami gyorsabb volt, mint vártam.', 'Sérülés utáni rehabilitációs programok személyre szabva, hogy gyorsan és biztonságosan térj vissza.'),
(56, 'Mária Horváth', 'mhorvath@example.com', 'mhorvath123', 'Debrecen, Hungary', 'Fogyás, Erőnléti edzés', 'Személyes', '5400 HUF/óra', 'Magyar', 'Egyik legjobb döntésem volt, hogy vele dolgozom!', 'Edzésprogramjaim segítenek a fogyásban és az erőnlét javításában egyaránt.'),
(57, 'Bence Kovács', 'bkovacs@example.com', 'bkovacs123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '6000 HUF/óra', 'Magyar', 'Nagyon jól felépített edzésekkel segít abban, hogy még erősebb legyek.', 'A személyre szabott erőnléti edzéseim segítenek abban, hogy elérd a legjobb formádat.'),
(58, 'Dóra Varga', 'dvarga@example.com', 'dvarga123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '5100 HUF/óra', 'Magyar', 'Segített abban, hogy sikeresen le tudtam fogyni!', 'A célom, hogy segítsek az embereknek az egészséges életmód kialakításában.'),
(59, 'Róbert Molnár', 'rmolnar@example.com', 'rmolnar123', 'Győr, Hungary', 'Rehabilitáció', 'Személyes', '6400 HUF/óra', 'Magyar', 'Rendkívül türelmes és hozzáértő edző.', 'Rehabilitációs programjaim segítenek a gyors regenerálódásban és a sérülések megelőzésében.'),
(60, 'Ádám Farkas', 'afarkas@example.com', 'afarkas123', 'Debrecen, Hungary', 'Fogyás', 'Személyes', '5300 HUF/óra', 'Magyar', 'Nagyon segítőkész és jól motivál, hogy elérjem a céljaimat.', 'A fogyás során segítek az étkezési szokások kialakításában és a személyre szabott edzésben.'),
(61, 'Tímea Kiss', 'tkiss@example.com', 'tkiss123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5600 HUF/óra', 'Magyar', 'Nagyon motiváló és alapos edző.', 'Edzéseim során kiemelt figyelmet fordítok a helyes technikára és a személyre szabott fejlődésre.'),
(62, 'Zoltán Tóth', 'ztoth@example.com', 'ztoth123', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '6000 HUF/óra', 'Magyar', 'Segített visszanyerni a mozgásképességemet sérülés után.', 'Rehabilitációs programjaim segítenek a gyors és biztonságos gyógyulásban.'),
(63, 'András Horváth', 'ahorvath@example.com', 'ahorvath123', 'Győr, Hungary', 'Fogyás', 'Személyes', '5300 HUF/óra', 'Magyar', 'Kitűnő edző, aki segít a motivációban és az eredmények elérésében.', 'Fogyás során a legfontosabb, hogy a mozgás és a táplálkozás harmóniáját megteremtsük.'),
(64, 'Krisztina Nagy', 'knagy@example.com', 'knagy123', 'Budapest, Hungary', 'Erőnléti edzés', 'Személyes', '5500 HUF/óra', 'Magyar', 'Minden edzés szórakoztató és kihívást jelentett.', 'Az erőnléti edzés során a folyamatos fejlődés elérése a célom.'),
(65, 'László Papp', 'lpapp@example.com', 'lpapp123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '6200 HUF/óra', 'Magyar', 'Minden edzés rendkívül alapos és segítőkész volt.', 'A rehabilitációs programok során figyelek a személyre szabott igényekre és fejlődésre.'),
(66, 'Anett Kiss', 'akiss@example.com', 'akiss123', 'Szeged, Hungary', 'Fogyás, Erőnléti edzés', 'Személyes', '5000 HUF/óra', 'Magyar', 'Nagyon jó tanácsokat kaptam a fogyásomhoz és az edzéseimhez.', 'A célom, hogy elérd a legjobb formádat, miközben fenntartjuk a motivációt.'),
(67, 'Bence Szabó', 'bszabo@example.com', 'bszabo123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5800 HUF/óra', 'Magyar', 'Kiváló edzés, minden nap éreztem a fejlődést.', 'Az edzéseken a személyes céljaidhoz igazítom a programot a maximális eredmény érdekében.'),
(68, 'Lilla Kovács', 'lkovacs@example.com', 'lkovacs123', 'Budapest, Hungary', 'Súlyzós edzés', 'Személyes', '6000 HUF/óra', 'Magyar', 'Nagyon motiváló és segítőkész edző!', 'A súlyzós edzés során arra koncentrálok, hogy a legjobb eredményeket érjük el a technika pontos alkalmazásával.'),
(69, 'Gábor Kocsis', 'gkocsis@example.com', 'gkocsis123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '5900 HUF/óra', 'Magyar', 'Gyorsan visszanyertem a mozgásomat a segítségével.', 'Rehabilitációs szakemberként a célom, hogy a lehető leghamarabb visszatérj a megszokott életedhez.'),
(70, 'Boglárka Szilágyi', 'bszilagyi@example.com', 'bszilagyi123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5700 HUF/óra', 'Magyar', 'Nagyon jól felépített edzésekkel segített a fejlődésemben.', 'Erőnléti edzéseimen minden egyes mozdulatra odafigyelek, hogy maximális eredményt érjünk el.'),
(71, 'Péter Kovács', 'pkovacs@example.com', 'pkovacs123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '5000 HUF/óra', 'Magyar', 'Rendkívül segítőkész edző, aki mindent megtesz az eredmények érdekében.', 'A fogyás az én szakterületem, segítek abban, hogy elérd a legjobb formádat.'),
(72, 'Mária Sándor', 'msandor@example.com', 'msandor123', 'Győr, Hungary', 'Rehabilitáció', 'Személyes', '6000 HUF/óra', 'Magyar', 'Minden edzés segített abban, hogy gyorsabban felépüljek.', 'A rehabilitáció során mindig figyelek a fokozatosságra és a helyes gyógyulásra.');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `trainers`
--
ALTER TABLE `trainers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `trainers`
--
ALTER TABLE `trainers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
