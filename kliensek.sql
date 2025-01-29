-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2025. Jan 22. 11:57
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
-- Tábla szerkezet ehhez a táblához `kliensek`
--

CREATE TABLE `kliensek` (
  `id` int(11) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- A tábla adatainak kiíratása `kliensek`
--

INSERT INTO `kliensek` (`id`, `full_name`, `age`, `email`, `password`) VALUES
(1, 'László Kiss', 30, 'lkiss@example.com', 'lkiss123'),
(2, 'Anna Szabó', 25, 'aszabo@example.com', 'aszabo123'),
(3, 'Béla Horváth', 28, 'bhorvath@example.com', 'bhorvath123'),
(4, 'Péter Varga', 35, 'pvarga@example.com', 'pvarga123'),
(5, 'Dávid Farkas', 40, 'dfarkas@example.com', 'dfarkas123'),
(6, 'Zsófia Szabó', 32, 'zszabo1@example.com', 'zszabo123'),
(7, 'Tamás Nagy', 50, 'tnagy@example.com', 'tnagy123'),
(8, 'Emese Tóth', 27, 'etoth@example.com', 'etoth123'),
(9, 'Károly Kiss', 60, 'kkiss@example.com', 'kkiss123'),
(10, 'Mária Horváth', 45, 'mhorvath1@example.com', 'mhorvath123'),
(11, 'Bence Kovács', 33, 'bkovacs@example.com', 'bkovacs123'),
(12, 'Dóra Varga', 24, 'dvarga@example.com', 'dvarga123'),
(13, 'Róbert Molnár', 29, 'rmolnar@example.com', 'rmolnar123'),
(14, 'Anita Kiss', 38, 'akiss1@example.com', 'akiss123'),
(15, 'Ádám Farkas', 41, 'afarkas@example.com', 'afarkas123'),
(16, 'Tímea Kiss', 36, 'tkiss@example.com', 'tkiss123'),
(17, 'Zoltán Tóth', 31, 'ztoth@example.com', 'ztoth123'),
(18, 'András Horváth', 29, 'ahorvath@example.com', 'ahorvath123'),
(19, 'Krisztina Nagy', 22, 'knagy@example.com', 'knagy123'),
(20, 'László Papp', 55, 'lpapp@example.com', 'lpapp123'),
(21, 'Anett Kiss', 37, 'akiss2@example.com', 'akiss123'),
(22, 'Bence Szabó', 26, 'bszabo@example.com', 'bszabo123'),
(23, 'Lilla Kovács', 29, 'lkovacs@example.com', 'lkovacs123'),
(24, 'Gábor Kocsis', 49, 'gkocsis@example.com', 'gkocsis123'),
(25, 'Boglárka Szilágyi', 34, 'bszilagyi@example.com', 'bszilagyi123'),
(26, 'Péter Kovács', 27, 'pkovacs@example.com', 'pkovacs123'),
(27, 'Mária Sándor', 47, 'msandor@example.com', 'msandor123'),
(28, 'Zoltán Fekete', 58, 'zfekete@example.com', 'zfekete123'),
(29, 'Eszter Lukács', 29, 'elukacs@example.com', 'elukacs123'),
(30, 'József Fodor', 44, 'jfodor@example.com', 'jfodor123'),
(31, 'Katalin Varga', 38, 'kvarga@example.com', 'kvarga123'),
(32, 'Miklós Szabó', 36, 'mszabo@example.com', 'mszabo123'),
(33, 'Szilvia Kocsis', 42, 'skocsis@example.com', 'skocsis123'),
(34, 'Rita Tóth', 28, 'rtoth@example.com', 'rtoth123'),
(35, 'Imre Horváth', 31, 'ihorvath@example.com', 'ihorvath123'),
(36, 'Csaba Papp', 41, 'cpapp@example.com', 'cpapp123'),
(37, 'Zsuzsanna Kovács', 33, 'zkovacs@example.com', 'zkovacs123'),
(38, 'Krisztián Kovács', 28, 'kkovacs1@example.com', 'kkovacs123'),
(39, 'Gergely Nagy', 30, 'gnagy@example.com', 'gnagy123'),
(40, 'Andrea Varga', 24, 'avarga@example.com', 'avarga123'),
(41, 'Judit Farkas', 27, 'jfarkas@example.com', 'jfarkas123'),
(42, 'Viktor Szabó', 34, 'vszabo@example.com', 'vszabo123'),
(43, 'László Tóth', 51, 'ltoth@example.com', 'ltoth123'),
(44, 'Réka Szilágyi', 32, 'rszilagyi@example.com', 'rszilagyi123'),
(45, 'Zoltán Szabó', 45, 'zszabo2@example.com', 'zszabo123'),
(46, 'Fanni Papp', 36, 'fpapp@example.com', 'fpapp123'),
(47, 'Erzsébet Fekete', 40, 'efekete@example.com', 'efekete123'),
(48, 'János Molnár', 39, 'jmolnar@example.com', 'jmolnar123'),
(49, 'Márton Horváth', 26, 'mhorvath2@example.com', 'mhorvath123'),
(50, 'Krisztina Farkas', 25, 'kfarkas@example.com', 'kfarkas123'),
(51, 'Tibor Kiss', 50, 'tkiss1@example.com', 'tkiss123'),
(52, 'Ilona Papp', 28, 'ipapp@example.com', 'ipapp123'),
(53, 'Zoltán Nagy', 55, 'znagy@example.com', 'znagy123'),
(54, 'Mária Kiss', 38, 'mkiss@example.com', 'mkiss123'),
(55, 'Norbert Tóth', 31, 'ntoth@example.com', 'ntoth123'),
(56, 'Tímea Szabó', 41, 'tszabo@example.com', 'tszabo123'),
(57, 'László Fodor', 46, 'lfodor@example.com', 'lfodor123'),
(58, 'József Papp', 52, 'jpapp@example.com', 'jpapp123');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `kliensek`
--
ALTER TABLE `kliensek`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `kliensek`
--
ALTER TABLE `kliensek`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
