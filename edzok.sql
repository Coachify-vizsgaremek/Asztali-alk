-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2025. Feb 12. 11:03
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
(1, 'John Doe', 'johndoe@example.com', 'johndoe123', 'Budapest, Hungary', 'Fogyás', 'Személyes', '5000', 'Magyar, Angol', NULL, 'A célom, hogy segítsek másoknak a fogyásban és az egészséges életmód kialakításában.'),
(2, 'Jane Smith', 'janesmith@example.com', 'janesmith123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar, Angol, Német', NULL, 'A rehabilitáció és a prevenció a szakterületem, hiszek a mozgás gyógyító erejében.'),
(3, 'Mark Johnson', 'markjohnson@example.com', 'markjohnson123', 'Online', 'Erőnléti edzés', 'Személyes', '4000', 'Angol', NULL, 'Erőnléti edzéseim során a személyre szabott programok és folyamatos visszajelzés a kulcs.'),
(4, 'Laura White', 'laurawhite@example.com', 'laurawhite123', 'Pécs, Hungary', 'Fogyás, Erőnléti edzés', 'Személyes', '5500', 'Magyar, Angol', NULL, 'Kombinálom az erőnléti és fogyási edzéseket, hogy mindenki elérje az optimális eredményt.'),
(5, 'Robert Brown', 'robertbrown@example.com', 'robertbrown123', 'Székesfehérvár, Hungary', 'Rehabilitáció, Erőnléti edzés', 'Személyes', '7000', 'Magyar, Angol', NULL, 'Rehabilitációs szakemberként az a célom, hogy visszavezesselek a legjobb formádba.'),
(6, 'Emily Clark', 'emilyclark@example.com', 'emilyclark123', 'Budapest, Hungary', 'Fogyás', 'Személyes', '4500', 'Magyar, Angol, Német', NULL, 'A személyre szabott fogyásprogramok mellett segítek a helyes étrend kialakításában.'),
(7, 'David Lee', 'davidlee@example.com', 'davidlee123', 'Online', 'Erőnléti edzés', 'Személyes', '4800', 'Angol', NULL, 'Az erőnléti edzésben az alapok és a progresszió elengedhetetlenek, de mindig figyelek a megfelelő technikára.'),
(8, 'Sophia Miller', 'sophiamiller@example.com', 'sophiamiller123', 'Győr, Hungary', 'Rehabilitáció', 'Személyes', '6200', 'Magyar, Angol', NULL, 'Minden esetben a sérülések utáni rehabilitációra koncentrálok, hogy biztonságosan térj vissza a mozgásba.'),
(9, 'Daniel Harris', 'danielharris@example.com', 'danielharris123', 'Online', 'Erőnléti edzés', 'Személyes', '5000', 'Angol', NULL, 'Az edzéseimet online tartom, ahol a közvetlen visszajelzés és a személyre szabott terv a kulcs a fejlődéshez.'),
(10, 'Olivia Martinez', 'oliviamartinez@example.com', 'oliviamartinez123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '4700', 'Magyar, Angol', NULL, 'A fogyás és a zsírégetés elérése érdekében intenzív edzéseket biztosítok a legjobb eredményekért.'),
(11, 'James Wilson', 'jameswilson@example.com', 'jameswilson123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '5300', 'Magyar, Angol', NULL, 'A rehabilitációs programok során mindig figyelek a testem jeleire, hogy a legjobban fejlődhessenek.'),
(12, 'Ava Davis', 'avdavis@example.com', 'avdavis123', 'Online', 'Fogyás', 'Személyes', '4900', 'Magyar, Angol, Olasz', NULL, 'Személyre szabott programot biztosítok, hogy mindenkinek a legjobb eredményt nyújtsam a fogyás terén.'),
(13, 'Michael Robinson', 'michaelrobinson@example.com', 'michaelrobinson123', 'Szeged, Hungary', 'Erőnléti edzés', 'Személyes', '5800', 'Magyar, Angol', NULL, 'Az erőnléti edzésben a célom, hogy mindenki maximalizálja saját teljesítményét.'),
(14, 'Anna Walker', 'annawalker@example.com', 'annawalker123', 'Budapest, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar, Angol', NULL, 'Sérülések utáni rehabilitációra specializálódtam, hogy mindenki teljesen visszanyerje mozgékonyságát.'),
(15, 'Ethan Lee', 'ethanlee@example.com', 'ethanlee123', 'Online', 'Erőnléti edzés', 'Személyes', '5500', 'Magyar, Angol', NULL, 'A célom, hogy minden egyes edzés során előrelépjünk és a fejlődés folyamatos legyen.'),
(16, 'Zoltán Varga', 'zvarga@example.com', 'zvarga123', 'Budapest, Hungary', 'Súlyzós edzés', 'Személyes', '5500', 'Magyar', NULL, 'Minden edzésnél a pontos technika és a folyamatos fejlődés a fő célom.'),
(17, 'Gábor Kovács', 'gkovacs@example.com', 'gkovacs123', 'Pécs, Hungary', 'Fogyás', 'Személyes', '5000', 'Magyar', NULL, 'A mozgás és a táplálkozás harmóniájára helyezem a hangsúlyt a céljaid eléréséhez.'),
(18, 'Eszter Farkas', 'efarkas@example.com', 'efarkas123', 'Székesfehérvár, Hungary', 'Erőnléti edzés', 'Személyes', '6000', 'Magyar', NULL, 'Erőnléti edzésen a célom a stabil alapok megteremtése és a folyamatos fejlődés.'),
(19, 'Katalin Papp', 'kpapp@example.com', 'kpapp123', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '5800', 'Magyar', NULL, 'Szakterületem a rehabilitáció, hogy minél gyorsabban vissza tudd nyerni a mozgékonyságodat.'),
(20, 'László Nagy', 'lnagy@example.com', 'lnagy123', 'Győr, Hungary', 'Súlyzós edzés', 'Személyes', '5900', 'Magyar', NULL, 'Súlyzós edzéseim során az intenzitás és a helyes végrehajtás kulcsfontosságú.'),
(21, 'Nóra Kiss', 'nkiss@example.com', 'nkiss123', 'Budapest, Hungary', 'Fogyás', 'Személyes', '5200', 'Magyar', NULL, 'A legjobb eredményekhez személyre szabott programokat kínálok, hogy gyorsan elérd a kívánt célt.'),
(22, 'Béla Tóth', 'btoth@example.com', 'btoth123', 'Debrecen, Hungary', 'Erőnléti edzés', 'Személyes', '5400', 'Magyar', NULL, 'Erőnléti edzéseim célja a folyamatos teljesítménynövelés és a megfelelő pihenési idő beállítása.'),
(23, 'Anikó Kovács', 'akovacs@example.com', 'akovacs123', 'Szeged, Hungary', 'Súlyzós edzés', 'Személyes', '5500', 'Magyar', NULL, 'A súlyzós edzés és a megfelelő étkezés biztosítja az optimális fejlődést minden egyes edző számára.'),
(49, 'Béla Horváth', 'bhorvath@example.com', 'bhorvath123', 'Budapest, Hungary', 'Súlyzós edzés', 'Személyes', '6000', 'Magyar', NULL, 'Súlyzós edzés közben figyelek a pontos technikai kivitelezésre és a fokozatosságra.'),
(50, 'Péter Varga', 'pvarga@example.com', 'pvarga123', 'Debrecen, Hungary', 'Fogyás', 'Személyes', '5200', 'Magyar', NULL, 'Fogyás és zsírégetés, folyamatos fejlődés a legfontosabb számomra.'),
(51, 'Dávid Farkas', 'dfarkas@example.com', 'dfarkas123', 'Pécs, Hungary', 'Rehabilitáció', 'Személyes', '6300', 'Magyar', NULL, 'A rehabilitációban a fokozatosságot és a megfelelő pihenőt helyezem előtérbe.'),
(52, 'Zsófia Szabó', 'zszabo@example.com', 'zszabo123', 'Székesfehérvár, Hungary', 'Erőnléti edzés', 'Személyes', '5500', 'Magyar', NULL, 'Edzéseim középpontjában az erőnléti fejlődés és a hatékony munkavégzés áll.'),
(53, 'Tamás Nagy', 'tnagy@example.com', 'tnagy123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '5100', 'Magyar', NULL, 'Személyre szabott edzésekkel segítek elérni a fogyási céljaidat.'),
(54, 'Emese Tóth', 'etoth@example.com', 'etoth123', 'Győr, Hungary', 'Erőnléti edzés', 'Személyes', '5600', 'Magyar', NULL, 'A célom, hogy minden edzés után látványos fejlődést tapasztalj a testépítésben.'),
(55, 'Károly Kiss', 'kkiss@example.com', 'kkiss123', 'Budapest, Hungary', 'Rehabilitáció', 'Személyes', '5800', 'Magyar', NULL, 'Sérülés utáni rehabilitációs programok személyre szabva, hogy gyorsan és biztonságosan térj vissza.'),
(56, 'Mária Horváth', 'mhorvath@example.com', 'mhorvath123', 'Debrecen, Hungary', 'Fogyás, Erőnléti edzés', 'Személyes', '5400', 'Magyar', NULL, 'Edzésprogramjaim segítenek a fogyásban és az erőnlét javításában egyaránt.'),
(57, 'Bence Kovács', 'bkovacs@example.com', 'bkovacs123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '6000', 'Magyar', NULL, 'A személyre szabott erőnléti edzéseim segítenek abban, hogy elérd a legjobb formádat.'),
(58, 'Dóra Varga', 'dvarga@example.com', 'dvarga123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '5100', 'Magyar', NULL, 'A célom, hogy segítsek az embereknek az egészséges életmód kialakításában.'),
(59, 'Róbert Molnár', 'rmolnar@example.com', 'rmolnar123', 'Győr, Hungary', 'Rehabilitáció', 'Személyes', '6400', 'Magyar', NULL, 'Rehabilitációs programjaim segítenek a gyors regenerálódásban és a sérülések megelőzésében.'),
(60, 'Ádám Farkas', 'afarkas@example.com', 'afarkas123', 'Debrecen, Hungary', 'Fogyás', 'Személyes', '5300', 'Magyar', NULL, 'A fogyás során segítek az étkezési szokások kialakításában és a személyre szabott edzésben.'),
(61, 'Tímea Kiss', 'tkiss@example.com', 'tkiss123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5600', 'Magyar', ' | Vélemény 1: Nagyon figyelmes és segítőkész! | Vélemény 2: Az edzések mindig változatosak! | Vélemény 3: Tökéletesen segít elérni a céljaimat! | Vélemény 4: Nagyon motiváló! | Vélemény 5: Minden edzés után új energiával töltődöm!', 'Edzéseim során kiemelt figyelmet fordítok a helyes technikára és a személyre szabott fejlődésre.'),
(62, 'Zoltán Tóth', 'ztoth@example.com', 'ztoth123', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar', ' | Vélemény 1: Nagyon jól megtervezett edzéstervek! | Vélemény 2: Az edzések mindig friss kihívásokat jelentenek! | Vélemény 3: Motiváló és segítőkész edző! | Vélemény 4: Kiváló szakember! | Vélemény 5: Az edzések mindig szórakoztatóak!', 'Rehabilitációs programjaim segítenek a gyors és biztonságos gyógyulásban.'),
(63, 'András Horváth', 'ahorvath@example.com', 'ahorvath123', 'Győr, Hungary', 'Fogyás', 'Személyes', '5300', 'Magyar', ' | Vélemény 1: Minden edzés egy új élmény! | Vélemény 2: Nagyon motiváló edző! | Vélemény 3: Az edzések mindig izgalmasak! | Vélemény 4: Segít a fejlődésben! | Vélemény 5: A legjobb edző, akit valaha választottam!', 'Fogyás során a legfontosabb, hogy a mozgás és a táplálkozás harmóniáját megteremtsük.'),
(64, 'Krisztina Nagy', 'knagy@example.com', 'knagy123', 'Budapest, Hungary', 'Erőnléti edzés', 'Személyes', '5500', 'Magyar', ' | Vélemény 1: Szuper edző, minden edzés után fejlődök! | Vélemény 2: Kiváló edzéstervek, mindig változatosak! | Vélemény 3: Segít elérni a céljaimat! | Vélemény 4: Nagyon motiváló és segítőkész! | Vélemény 5: Minden edzés más élmény!', 'Az erőnléti edzés során a folyamatos fejlődés elérése a célom.'),
(65, 'László Papp', 'lpapp@example.com', 'lpapp123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '6200', 'Magyar', ' | Vélemény 1: Nagyon jól magyaráz el mindent! | Vélemény 2: Az edzések mindig szórakoztatóak és hasznosak! | Vélemény 3: Kiváló edző, segít a fejlődésben! | Vélemény 4: Motiváló és eredményes edzések! | Vélemény 5: Minden edzés után elégedett vagyok!', 'A rehabilitációs programok során figyelek a személyre szabott igényekre és fejlődésre.'),
(66, 'Anett Kiss', 'akiss@example.com', 'akiss123', 'Szeged, Hungary', 'Fogyás, Erőnléti edzés', 'Személyes', '5000', 'Magyar', ' | Vélemény 1: Tökéletes edző, mindig segít a fejlődésben! | Vélemény 2: Az edzések mindig izgalmasak és hatékonyak! | Vélemény 3: Maximálisan elégedett vagyok! | Vélemény 4: Nagyon szórakoztató edzések! | Vélemény 5: Kiváló szakember!', 'A célom, hogy elérd a legjobb formádat, miközben fenntartjuk a motivációt.'),
(67, 'Bence Szabó', 'bszabo@example.com', 'bszabo123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5800', 'Magyar', ' | Vélemény 1: Nagyon segítőkész és figyelmes! | Vélemény 2: Az edzések minden alkalommal egyre jobbak! | Vélemény 3: Motiváló és szórakoztató! | Vélemény 4: Segít elérni a céljaimat! | Vélemény 5: Az edzések mindig hasznosak!', 'Az edzéseken a személyes céljaidhoz igazítom a programot a maximális eredmény érdekében.'),
(68, 'Lilla Kovács', 'lkovacs@example.com', 'lkovacs123', 'Budapest, Hungary', 'Súlyzós edzés', 'Személyes', '6000', 'Magyar', ' | Vélemény 1: A legjobb edző, akit választottam! | Vélemény 2: Nagyon jól megtervezett edzéstervek! | Vélemény 3: Segít a fejlődésben és motivál! | Vélemény 4: Az edzések mindig eredményesek! | Vélemény 5: Nagyon szórakoztató edzéseken veszek részt!', 'A súlyzós edzés során arra koncentrálok, hogy a legjobb eredményeket érjük el a technika pontos alkalmazásával.'),
(69, 'Gábor Kocsis', 'gkocsis@example.com', 'gkocsis123', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '5900', 'Magyar', ' | Vélemény 1: Kiváló szakember! | Vélemény 2: Az edzések mindig szórakoztatóak és eredményesek! | Vélemény 3: Motiváló edző! | Vélemény 4: Nagyon segít a fejlődésemben! | Vélemény 5: Tökéletes edző!', 'Rehabilitációs szakemberként a célom, hogy a lehető leghamarabb visszatérj a megszokott életedhez.'),
(70, 'Boglárka Szilágyi', 'bszilagyi@example.com', 'bszilagyi123', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5700', 'Magyar', ' | Vélemény 1: Nagyon szórakoztató edzések! | Vélemény 2: Minden edzés után jobban érzem magam! | Vélemény 3: Az edzések mindig kihívást jelentenek! | Vélemény 4: Segít a céljaim elérésében! | Vélemény 5: Motiváló és segítőkész edző!', 'Erőnléti edzéseimen minden egyes mozdulatra odafigyelek, hogy maximális eredményt érjünk el.'),
(71, 'Péter Kovács', 'pkovacs@example.com', 'pkovacs123', 'Szeged, Hungary', 'Fogyás', 'Személyes', '5000', 'Magyar', ' | Vélemény 1: Kiváló edző, minden edzés eredményes! | Vélemény 2: Az edzések mindig szórakoztatóak! | Vélemény 3: Nagyon jól motivál! | Vélemény 4: Az edzések mindig változatosak! | Vélemény 5: Maximálisan elégedett vagyok!', 'A fogyás az én szakterületem, segítek abban, hogy elérd a legjobb formádat.'),
(72, 'Mária Sándor', 'msandor@example.com', 'msandor123', 'Győr, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar', ' | Vélemény 1: Kitűnő edző! | Vélemény 2: Motiváló és szaktudása kiemelkedő! | Vélemény 3: Az edzések mindig élvezetesek! | Vélemény 4: Személyre szabott figyelmet kapok! | Vélemény 5: Tökéletesen megtervezett programok!', 'A rehabilitáció során mindig figyelek a fokozatosságra és a helyes gyógyulásra.');

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
