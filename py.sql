-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 07, 2022 at 03:56 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uts_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `tanggota`
--

CREATE TABLE `tanggota` (
  `NIM` int(255) NOT NULL,
  `NamaMhs` varchar(255) NOT NULL,
  `Jurusan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tanggota`
--

INSERT INTO `tanggota` (`NIM`, `NamaMhs`, `Jurusan`) VALUES
(32190001, 'Welly Febriyanto Cen', 'TI'),
(32190002, 'Rico Fernando', 'TI');

-- --------------------------------------------------------

--
-- Table structure for table `tbuku`
--

CREATE TABLE `tbuku` (
  `KodeBuku` int(255) NOT NULL,
  `Judul` varchar(255) NOT NULL,
  `Stok` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbuku`
--

INSERT INTO `tbuku` (`KodeBuku`, `Judul`, `Stok`) VALUES
(1, 'beba', 12),
(2, 'asdasd', 11);

-- --------------------------------------------------------

--
-- Table structure for table `tkembali`
--

CREATE TABLE `tkembali` (
  `KodeKembali` int(255) NOT NULL,
  `KodeBuku` int(255) NOT NULL,
  `NIM` int(255) NOT NULL,
  `TglKembali` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `tkembali`
--
DELIMITER $$
CREATE TRIGGER `delete_masuk` AFTER DELETE ON `tkembali` FOR EACH ROW BEGIN
	UPDATE tbuku SET Stok = Stok - 1
    WHERE KodeBuku = OLD.KodeBuku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `t_masuk` AFTER INSERT ON `tkembali` FOR EACH ROW BEGIN
	UPDATE tbuku SET Stok = stok + 1
    WHERE KodeBuku = New.KodeBuku;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tpinjam`
--

CREATE TABLE `tpinjam` (
  `KodePinjam` int(255) NOT NULL,
  `KodeBuku` int(255) NOT NULL,
  `NIM` int(255) NOT NULL,
  `TglPinjam` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tpinjam`
--

INSERT INTO `tpinjam` (`KodePinjam`, `KodeBuku`, `NIM`, `TglPinjam`) VALUES
(4, 1, 32190001, '2022-04-07'),
(5, 2, 32190001, '2022-04-07');

--
-- Triggers `tpinjam`
--
DELIMITER $$
CREATE TRIGGER `delete` AFTER DELETE ON `tpinjam` FOR EACH ROW BEGIN
	UPDATE tbuku SET Stok = Stok+1
    WHERE KodeBuku = OLD.KodeBuku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `tkeluar` AFTER INSERT ON `tpinjam` FOR EACH ROW BEGIN
	UPDATE tbuku SET STOK = STOK - 1
    WHERE KodeBuku = NEW.KodeBuku;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tanggota`
--
ALTER TABLE `tanggota`
  ADD PRIMARY KEY (`NIM`);

--
-- Indexes for table `tbuku`
--
ALTER TABLE `tbuku`
  ADD PRIMARY KEY (`KodeBuku`);

--
-- Indexes for table `tkembali`
--
ALTER TABLE `tkembali`
  ADD PRIMARY KEY (`KodeKembali`),
  ADD KEY `KembaliBuku` (`KodeBuku`),
  ADD KEY `KembaliNIM` (`NIM`);

--
-- Indexes for table `tpinjam`
--
ALTER TABLE `tpinjam`
  ADD PRIMARY KEY (`KodePinjam`),
  ADD KEY `KodeBuku` (`KodeBuku`),
  ADD KEY `KodeBuku_2` (`KodeBuku`),
  ADD KEY `PinjamNIM` (`NIM`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tpinjam`
--
ALTER TABLE `tpinjam`
  MODIFY `KodePinjam` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tkembali`
--
ALTER TABLE `tkembali`
  ADD CONSTRAINT `KembaliBuku` FOREIGN KEY (`KodeBuku`) REFERENCES `tbuku` (`KodeBuku`),
  ADD CONSTRAINT `KembaliNIM` FOREIGN KEY (`NIM`) REFERENCES `tanggota` (`NIM`);

--
-- Constraints for table `tpinjam`
--
ALTER TABLE `tpinjam`
  ADD CONSTRAINT `PinjamBuku` FOREIGN KEY (`KodeBuku`) REFERENCES `tbuku` (`KodeBuku`),
  ADD CONSTRAINT `PinjamNIM` FOREIGN KEY (`NIM`) REFERENCES `tanggota` (`NIM`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
