-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2025. Ápr 15. 14:02
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
-- Adatbázis: `coachify_edzok`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `edzok`
--

CREATE TABLE `edzok` (
  `id` int(11) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `specialization` varchar(255) DEFAULT NULL,
  `available_training_types` varchar(255) DEFAULT NULL,
  `price_range` varchar(255) DEFAULT NULL,
  `languages` varchar(255) DEFAULT NULL,
  `reviews` text DEFAULT NULL,
  `introduction` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- A tábla adatainak kiíratása `edzok`
--

INSERT INTO `edzok` (`id`, `full_name`, `location`, `specialization`, `available_training_types`, `price_range`, `languages`, `reviews`, `introduction`) VALUES
(11, 'Jakab Vilmos', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '5300', 'Magyar, Angol', 'Egyéni szükségleteimhez igazított rehabilitációs tervet kaptam.', 'A rehabilitációs programok során mindig figyelek a testem jeleire, hogy a legjobban fejlődhessenek.'),
(12, 'Ava Davis', 'Online', 'Fogyás', 'Személyes', '4900', 'Magyar, Angol, Olasz', 'Segít a zsírégetésben és a mozgás örömében.', 'Személyre szabott programot biztosítok, hogy mindenkinek a legjobb eredményt nyújtsam a fogyás terén.'),
(13, 'Miklós Horváth', 'Szeged, Hungary', 'Erőnléti edzés', 'Személyes', '5800', 'Magyar, Angol', 'Nagyon jól érthető edzésprogramot készített számomra.', 'Az erőnléti edzésben a célom, hogy mindenki maximalizálja saját teljesítményét.'),
(14, 'Anna Walker', 'Budapest, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar, Angol', 'Sokat segített a mozgáskorlátozottságom leküzdésében.', 'Sérülések utáni rehabilitációra specializálódtam, hogy mindenki teljesen visszanyerje mozgékonyságát.'),
(16, 'Gréta Németh', 'Pécs, Hungary', 'Fogyás, Erőnléti edzés', 'Személyes', '5100', 'Magyar, Angol', 'Nagyon jól motivál, hogy a legjobb formámra törekedjek!', 'A kombinált programjaim segítenek mind a fogyásban, mind az erőnléti fejlődésben.'),
(17, 'Márk Nagy', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '5500', 'Magyar, Angol', 'Rendkívül hatékony rehabilitációs programok, amelyeket követve gyorsan jobban éreztem magam.', 'Rehabilitációs programjaim minden egyes lépését a legjobb eredmény érdekében személyre szabom.'),
(19, 'Judit Kiss', 'Veszprém, Hungary', 'Fogyás', 'Személyes', '4900', 'Magyar, Angol', 'Nagyon segítőkész és kedves edző, sokat segített a fogyásomban.', 'A fogyás során személyre szabott tanácsokat adok, hogy minél hatékonyabban érhesd el a céljaidat.'),
(20, 'Gábor Tóth', 'Miskolc, Hungary', 'Fogyás', 'Személyes', '5100', 'Magyar, Angol', 'Nagyon motiváló edző, aki segít a céljaim elérésében.', 'Fogyás és zsírégetés terén szerzett tapasztalataimmal segítek minden korosztálynak.'),
(21, 'Lilla Gulyás', 'Veszprém, Hungary', 'Erőnléti edzés', 'Személyes', '5500', 'Magyar, Angol', 'Kiváló programot állított össze, amely segített fejlesztenem az állóképességemet.', 'Az erőnléti edzés során mindig figyelek a megfelelő technikára és a fokozatos fejlődésre.'),
(22, 'András Farkas', 'Debrecen, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar, Angol', 'Kiváló rehabilitációs szakember, aki segített rehabilitálni a sérülésemet.', 'Sérülés utáni rehabilitációban és az újrakezdésben segítek a legmodernebb technikák alkalmazásával.'),
(23, 'Petra Molnár', 'Szeged, Hungary', 'Fogyás', 'Személyes', '5000', 'Magyar, Angol', 'Nagyon segítőkész, a céljaimra szabott programot kaptam.', 'A fogyás során segítek megváltoztatni az étkezési szokásokat és a napi rutint.'),
(24, 'Zoltán Kocsis', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5300', 'Magyar, Angol', 'Jó edző, akinek köszönhetően már most jobban érzem magam a bőrömben.', 'A testépítés és erőnléti edzés terén szerzett tapasztalataim segítenek a legjobb eredmény elérésében.'),
(25, 'László Simon', 'Sopron, Hungary', 'Rehabilitáció', 'Személyes', '6200', 'Magyar, Angol', 'Tökéletes rehabilitációs szakember, akinek az edzései segítettek a fájdalommentes mozgásban.', 'A rehabilitáció során figyelmet fordítok minden apró részletre, hogy a legjobb eredményeket érjük el.'),
(26, 'Zsuzsanna Nagy', 'Eger, Hungary', 'Fogyás', 'Személyes', '5400', 'Magyar, Angol', 'Nagyon segítőkész és motiváló edző, aki segített elérni a kitűzött céljaimat.', 'A célom, hogy minden ügyfelem számára elérhetővé tegyem a sikeres fogyást, miközben megtartják a motivációjukat.'),
(27, 'Miklós Horváth', 'Szeged, Hungary', 'Erőnléti edzés', 'Személyes', '5700', 'Magyar, Angol', 'Az edzései nemcsak fizikailag, hanem mentálisan is segítenek a fejlődésben.', 'A személyre szabott erőnléti edzések során mindenkinek segítek elérni a legjobb teljesítményt.'),
(28, 'Anna Székely', 'Sopron, Hungary', 'Rehabilitáció', 'Személyes', '5900', 'Magyar, Angol', 'Kiváló rehabilitációs szakember, akit mindenkinek ajánlok.', 'Rehabilitációs szakemberként mindig az ügyfeleim igényeihez igazítom a programokat.'),
(29, 'Tamás Fekete', 'Zalaegerszeg, Hungary', 'Fogyás', 'Személyes', '4800', 'Magyar, Angol', 'Nagyon segítőkész és támogató, mindvégig mellettem állt a céljaim elérésében.', 'A fogyás során segítek megtalálni az ideális mozgásformákat és diétát, hogy könnyedén elérd a céljaidat.'),
(30, 'Péter Sárközi', 'Békéscsaba, Hungary', 'Erőnléti edzés', 'Személyes', '6000', 'Magyar, Angol', 'Nagyon hatékony edző, aki segített elérni a maximális erőnlétemet.', 'Az erőnléti edzés az alapja mindennek, és én segítek mindenkinek elérni a legjobb formáját.'),
(31, 'László Ferenc', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '6400', 'Magyar, Angol', 'Segített a sérülésem utáni rehabilitációban, és sikeresen visszatértem a sporthoz.', 'A rehabilitáció és a sportorvosi tanácsadás a szakterületem, hogy mindenki teljesen visszatérhessen a mozgásba.'),
(32, 'Gabriella Tóth', 'Debrecen, Hungary', 'Fogyás', 'Személyes', '4700', 'Magyar, Angol', 'A programja segített sokkal fittebbé válni.', 'A fogyás és a megfelelő étkezés kombinációjával segítem a legjobb eredmények elérését.'),
(33, 'Gergely Károly', 'Budapest, Hungary', 'Erőnléti edzés', 'Személyes', '5500', 'Magyar, Angol', 'Nagyon segítőkész és motiváló, eredményes edzéseken vettem részt.', 'Személyre szabott erőnléti programokat biztosítok, hogy mindenki fejlődhessen a legjobb formájában.'),
(34, 'István Lakatos', 'Miskolc, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar, Angol', 'Segített nekem visszatérni a mozgáshoz a sérülésem után.', 'A rehabilitáció során mindig figyelek az egyéni igényekre, hogy biztonságosan és hatékonyan végezhessem el a gyógyulást.'),
(35, 'Klaudia Kálmán', 'Veszprém, Hungary', 'Fogyás', 'Személyes', '5100', 'Magyar, Angol', 'A legjobb edző, aki segített elérni a céljaimat, miközben folyamatosan támogatta a fejlődésemet.', 'A célom, hogy segítsek a zsírégetésben és az egészséges életmód kialakításában, hogy tartós eredményeket érj el.'),
(37, 'Fanni Király', 'Pécs, Hungary', 'Rehabilitáció', 'Személyes', '6300', 'Magyar, Angol', 'A rehabilitációs programjai segítettek nekem visszanyerni az erőmet és a mozgásképességemet.', 'Munkám során mindig személyre szabom a rehabilitációt, hogy gyorsan és biztonságosan visszatérj a legjobb formádba.'),
(38, 'Bálint Varga', 'Budapest, Hungary', 'Fogyás', 'Személyes', '4900', 'Magyar, Angol', 'Nagyon motiváló edző, aki mindig segít a céljaim elérésében.', 'A fogyás és zsírégetés érdekében kialakított programjaim segítenek az optimális eredmények elérésében.'),
(39, 'János Nagy', 'Zalaegerszeg, Hungary', 'Erőnléti edzés', 'Személyes', '5200', 'Magyar, Angol', 'Segített a kondícióm növelésében, és javított az erőnlétemen.', 'Az erőnléti edzések során figyelmes vagyok az egyéni szükségletekre és az edzés biztonságára.'),
(40, 'Krisztina Pál', 'Veszprém, Hungary', 'Rehabilitáció', 'Személyes', '5500', 'Magyar, Angol', 'Rendkívül hatékony rehabilitációs programot kaptam tőle, és sokkal jobban érzem magam.', 'A rehabilitáció során személyre szabott kezelésekkel segítem a gyógyulást, hogy gyorsan visszatérhess a sporthoz.'),
(41, 'Sándor Nagy', 'Győr, Hungary', 'Fogyás', 'Személyes', '4800', 'Magyar, Angol', 'Nagyon segítőkész és figyelmes edző, aki mindvégig mellettem állt a fogyásban.', 'Személyre szabott fogyásprogramjaimmal mindenki elérheti a legjobb eredményeket.'),
(42, 'Eszter Fodor', 'Budapest, Hungary', 'Fogyás', 'Személyes', '4900', 'Magyar, Angol', 'Nagyon segítőkész és motiváló, mindvégig támogatta a céljaimat.', 'A fogyás során segítek megtalálni az ideális mozgásformákat és étkezést, hogy a legjobb eredményt érjük el.'),
(43, 'Gábor Barna', 'Szeged, Hungary', 'Erőnléti edzés', 'Személyes', '5600', 'Magyar, Angol', 'Segített növelni az erőnlétemet és javítani a teljesítményemet.', 'A testépítés és erőnléti edzés kombinációjával érem el, hogy a legjobb eredményt hozd ki magadból.'),
(44, 'László Károly', 'Pécs, Hungary', 'Rehabilitáció', 'Személyes', '5900', 'Magyar, Angol', 'Kiváló rehabilitációs szakember, segített a fájdalommentes mozgásban.', 'A rehabilitációs programjaim segítenek abban, hogy gyorsan és biztonságosan visszatérj a sporthoz.'),
(45, 'Tímea Hegedűs', 'Sopron, Hungary', 'Fogyás', 'Személyes', '5300', 'Magyar, Angol', 'Rendkívül támogató és segítőkész, segített a fogyási céljaim elérésében.', 'A személyre szabott fogyási programokkal segítek abban, hogy sikeresen érhesd el a céljaidat.'),
(46, 'Zoltán Varga', 'Debrecen, Hungary', 'Erőnléti edzés', 'Személyes', '5500', 'Magyar, Angol', 'Segített a fizikális állapotom javításában, és már most erősebbnek érzem magam.', 'Az erőnléti edzéseim segítenek abban, hogy növeld az erődet és a fizikai állóképességedet.'),
(47, 'Krisztina Tóth', 'Veszprém, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar, Angol', 'Nagyon alapos és figyelmes rehabilitációs edző, aki segített helyreállítani a mozgásképességemet.', 'A rehabilitációs programjaim segítenek a legjobb állapotba kerülni, a fájdalommentes mozgás visszaállításában.'),
(48, 'Gergely Kocsis', 'Zalaegerszeg, Hungary', 'Fogyás', 'Személyes', '5100', 'Magyar, Angol', 'Szuper motiváló edző, aki segített a fogyásomban, miközben folyamatosan támogatta a fejlődésemet.', 'A célom, hogy segítsek mindenkinek elérni a legjobb eredményeket a fogyás terén, miközben megőrizzük a motivációt.'),
(49, 'Lilla Keresztes', 'Szeged, Hungary', 'Erőnléti edzés', 'Személyes', '5800', 'Magyar, Angol', 'Nagyon segítőkész és profi, segített fejleszteni az erőnlétemet.', 'A személyre szabott erőnléti edzés segít abban, hogy elérd a legjobb formádat, miközben biztonságosan végezzük el az edzéseket.'),
(50, 'Miklós Balogh', 'Pécs, Hungary', 'Rehabilitáció', 'Személyes', '6200', 'Magyar, Angol', 'Szuper rehabilitációs programokat dolgozott ki számomra, segítettek a mozgásom helyreállításában.', 'Rehabilitációs szakemberként figyelek a legújabb technikák alkalmazására a gyors és hatékony gyógyulás érdekében.'),
(51, 'Klaudia Szabó', 'Sopron, Hungary', 'Fogyás', 'Személyes', '5400', 'Magyar, Angol', 'Nagyon kedves és támogató edző, aki segített a fogyásban és az egészséges életmód kialakításában.', 'A fogyás és egészséges életmód mellett a legfontosabb a személyre szabott programok alkalmazása, amit mindig a céljaidra szabok.'),
(52, 'Tamás Farkas', 'Szeged, Hungary', 'Erőnléti edzés', 'Személyes', '5600', 'Magyar, Angol', 'Erőnléti edzés terén kiváló, segített megerősödni és jobban teljesíteni.', 'A személyre szabott erőnléti edzés segít a megfelelő fizikai állapot elérésében, miközben biztonságos technikákat alkalmazunk.'),
(53, 'József Kovács', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '6400', 'Magyar, Angol', 'Nagyon figyelmes és precíz rehabilitációs edző, segített a sérülésem utáni felépülésben.', 'Rehabilitációs programjaim célja, hogy a legjobb állapotba hozhassalak vissza, miközben minden lépést kontrollálok.'),
(54, 'Péter Sipos', 'Budapest, Hungary', 'Fogyás', 'Személyes', '4900', 'Magyar, Angol', 'Segített elérni a céljaimat a fogyás terén, mindig támogató és motiváló volt.', 'A fogyás egy hosszú távú folyamat, és segítek abban, hogy ezen az úton ne veszítsd el a motivációt.'),
(55, 'Mária Molnár', 'Győr, Hungary', 'Erőnléti edzés', 'Személyes', '5100', 'Magyar, Angol', 'Már rövid idő alatt látható eredményeket értünk el, és minden edzés inspiráló volt.', 'A célom, hogy segítsek mindenkinek elérni a legjobb erőnlétet és testformát.'),
(56, 'Dániel Tóti', 'Zalaegerszeg, Hungary', 'Rehabilitáció', 'Személyes', '5700', 'Magyar, Angol', 'Nagyon figyelmes és segítőkész rehabilitációs edző, gyorsan helyreállítottam a mozgásképességemet.', 'A rehabilitáció során mindig figyelek a legújabb technológiák alkalmazására a gyors gyógyulás érdekében.'),
(57, 'Noémi Kiss', 'Pécs, Hungary', 'Fogyás', 'Személyes', '5000', 'Magyar, Angol', 'Nagyon segítőkész edző, aki támogatott minden lépésben, hogy elérjem a fogyási céljaimat.', 'Segítek a fogyásban a megfelelő étrend és mozgásformák kiválasztásával.'),
(58, 'Zsolt Horváth Péter', 'Miskolc, Hungary', 'Erőnléti edzés', 'Személyes', '5300', 'Magyar, Angol', 'Tudja, hogyan érhetem el a legjobb erőnlétet, és mindig figyel a biztonságra.', 'Erőnléti edzés segítségével elérheted a legjobb fizikai formát és állóképességet.'),
(60, 'László Németh', 'Sopron, Hungary', 'Fogyás', 'Személyes', '5100', 'Magyar, Angol', 'Nagyon támogató edző, aki segített a fogyásban és az egészséges életmódban.', 'A fogyás során segítek a helyes táplálkozásban és az ideális mozgásformák kiválasztásában.'),
(61, 'Judit Varga', 'Pécs, Hungary', 'Erőnléti edzés', 'Személyes', '5400', 'Magyar, Angol', 'Erőnléti edzésben segített növelni az állóképességemet, és mindvégig támogatott.', 'Az erőnléti edzés során mindig a legjobb formád elérésére koncentrálunk.'),
(62, 'Erzsébet Lakatos', 'Szeged, Hungary', 'Rehabilitáció', 'Személyes', '6200', 'Magyar, Angol', 'Segített a rehabilitációs folyamatban, gyorsan és hatékonyan helyreálltam.', 'A rehabilitációs programjaim segítenek, hogy visszanyerd a teljes mozgásképességedet és gyorsan felépülj.'),
(63, 'László Sárközi', 'Veszprém, Hungary', 'Fogyás', 'Személyes', '5000', 'Magyar, Angol', 'Nagyon támogató edző, aki segített a fogyásban, miközben folyamatosan motivált.', 'Segítek, hogy a fogyás ne legyen nehéz feladat, és elérd a legjobb eredményeket.'),
(64, 'Nóra Pál', 'Győr, Hungary', 'Erőnléti edzés', 'Személyes', '5600', 'Magyar, Angol', 'Már most eredményeket láthatok, és sokkal jobban érzem magam az edzések után.', 'Az erőnléti edzés célja, hogy javítsuk az állóképességedet és elérd a legjobb fizikai formát.'),
(65, 'Miklós Kálmán', 'Budapest, Hungary', 'Rehabilitáció', 'Személyes', '6000', 'Magyar, Angol', 'Nagyon segítőkész rehabilitációs edző, aki segített a gyorsabb felépülésben.', 'A rehabilitáció során figyelek a helyes mozgásra és technikákra, hogy gyorsan és biztonságosan gyógyulj meg.');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `edzok`
--
ALTER TABLE `edzok`
  ADD PRIMARY KEY (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `edzok`
--
ALTER TABLE `edzok`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
