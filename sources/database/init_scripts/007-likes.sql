DROP TABLE IF EXISTS Likes;

CREATE TABLE IF NOT EXISTS Likes(
id INT AUTO_INCREMENT,
post_id INT NOT NULL,
author VARCHAR(255) NOT NULL,
timestamp DATETIME NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (post_id) REFERENCES Posts(id) ON DELETE CASCADE,
FOREIGN KEY (author) REFERENCES Users(username) ON UPDATE CASCADE ON DELETE CASCADE
);

DELIMITER //
CREATE TRIGGER CreateLikeNotification
    AFTER INSERT ON Likes
    FOR EACH ROW
    BEGIN
        INSERT INTO Notifications (id, type, status) VALUES (NEW.id, 'like', 'unread');
		END; //
DELIMITER ;

INSERT INTO Likes (id, post_id, author, timestamp)
VALUES
(8, 981, "CosmicCougar",'2023-02-01 04:09:06'),
(15, 940, "SapphireSparrow",'2023-04-05 07:21:39'),
(16, 910, "MysticMandrill",'2023-02-17 18:16:49'),
(31, 907, "EnchantedElkhound",'2023-03-03 11:16:59'),
(40, 902, "RadiantRat",'2023-02-01 07:42:02'),
(50, 901, "ElectricEchidna",'2023-04-06 13:49:32'),
(54, 882, "LunarLemming",'2023-04-07 18:21:27'),
(56, 870, "VelvetVole",'2023-03-21 23:08:59'),
(72, 837, "FieryFrigatebird",'2023-03-03 07:50:11'),
(92, 810, "OceanicOcelot",'2023-03-25 05:45:27'),
(98, 809, "EnigmaticElk",'2023-03-11 17:20:22'),
(105, 804, "CrimsonCuckoo",'2023-01-15 03:09:25'),
(119, 801, "JadeJay",'2023-03-24 01:02:48'),
(159, 796, "MysticMole",'2023-03-03 04:57:08'),
(161, 792, "GalacticGorilla",'2023-01-31 06:43:57'),
(172, 790, "RadiantRhino",'2023-03-27 03:13:47'),
(191, 774, "SilverSwan",'2023-03-22 21:47:24'),
(196, 773, "CelestialCentipede",'2023-02-01 19:54:30'),
(205, 769, "CosmicChinchilla",'2023-01-18 01:17:26'),
(224, 768, "EnchantedEmperor",'2023-03-05 04:19:08'),
(239, 759, "FieryFlamingo",'2023-01-10 05:34:50'),
(245, 743, "StarryScorpion",'2023-03-26 21:03:23'),
(267, 742, "EmeraldEagle",'2023-03-07 00:55:55'),
(272, 737, "MysticMosquito",'2023-02-18 22:53:42'),
(276, 732, "ElectricEagleRay",'2023-01-30 13:56:35'),
(431, 595, "CelestialCentipede", '2023-01-17 13:00:23'),
(277, 731, "CosmicCougar", '2023-02-08 03:43:29'),
(280, 726, "SapphireSparrow", '2023-02-08 14:58:08'),
(295, 725, "MysticMandrill", '2023-02-22 04:23:17'),
(298, 724, "EnchantedElkhound", '2023-03-17 16:56:17'),
(300, 718, "RadiantRat", '2023-02-14 10:36:21'),
(305, 717, "ElectricEchidna", '2023-02-03 15:07:35'),
(313, 691, "LunarLemming", '2023-02-15 01:39:30'),
(314, 686, "VelvetVole", '2023-01-23 21:39:47'),
(325, 679, "FieryFrigatebird", '2023-02-19 23:51:33'),
(377, 659, "OceanicOcelot", '2023-02-01 18:31:21'),
(382, 658, "EnigmaticElk", '2023-03-31 02:04:08'),
(388, 644, "CrimsonCuckoo", '2023-03-31 05:35:17'),
(396, 638, "JadeJay", '2023-02-22 20:44:27'),
(410, 637, "MysticMole", '2023-01-06 10:34:48'),
(412, 617, "GalacticGorilla", '2023-02-22 05:21:46'),
(420, 616, "RadiantRhino", '2023-01-03 17:49:15'),
(425, 611, "SilverSwan", '2023-01-03 05:49:36'),
(444, 594, "CosmicChinchilla", '2023-02-13 15:34:09'),
(458, 573, "EnchantedEmperor", '2023-02-16 13:07:35'),
(468, 562, "FieryFlamingo", '2023-01-08 06:15:05'),
(485, 543, "StarryScorpion", '2023-02-25 18:00:44'),
(486, 540, "EmeraldEagle", '2023-04-04 06:53:11'),
(498, 536, "MysticMosquito", '2023-01-28 02:11:09'),
(525, 525, "ElectricEagleRay", '2023-03-22 22:11:45'),
(536, 498, "CosmicCougar", '2023-04-06 07:30:10'),
(540, 486, "SapphireSparrow", '2023-02-03 01:02:40'),
(543, 485, "MysticMandrill", '2023-03-31 12:36:33'),
(562, 468, "EnchantedElkhound", '2023-01-08 06:49:50'),
(573, 458, "RadiantRat", '2023-03-16 05:07:09'),
(594, 444, "ElectricEchidna", '2023-03-31 20:08:49'),
(595, 431, "LunarLemming", '2023-02-02 00:30:47'),
(611, 425, "VelvetVole", '2023-01-04 21:33:53'),
(616, 420, "FieryFrigatebird", '2023-02-24 12:57:36'),
(617, 412, "OceanicOcelot", '2023-02-04 06:26:59'),
(637, 410, "EnigmaticElk", '2023-03-11 16:28:06'),
(638, 396, "CrimsonCuckoo", '2023-03-05 18:17:29'),
(644, 388, "JadeJay", '2023-03-29 13:55:49'),
(658, 382, "MysticMole", '2023-02-08 14:05:43'),
(659, 377, "GalacticGorilla", '2023-01-19 09:10:12'),
(679, 325, "RadiantRhino", '2023-02-01 11:27:34'),
(686, 314, "SilverSwan", '2023-03-04 23:32:40'),
(691, 313, "CelestialCentipede", '2023-01-04 11:55:35'),
(717, 305, "CosmicChinchilla", '2023-04-02 20:38:50'),
(718, 300, "EnchantedEmperor", '2023-03-08 16:20:16'),
(724, 298, "FieryFlamingo", '2023-01-02 20:49:56'),
(725, 295, "StarryScorpion", '2023-01-15 11:31:20'),
(726, 280, "EmeraldEagle", '2023-01-14 17:24:42'),
(731, 277, "MysticMosquito", '2023-01-30 01:12:01'),
(732, 276, "ElectricEagleRay", '2023-01-30 13:24:59'),
(737, 272, "CosmicCougar", '2023-03-01 00:29:57'),
(742, 267, "SapphireSparrow", '2023-04-05 22:16:02'),
(743, 245, "MysticMandrill", '2023-02-01 16:37:14'),
(759, 239, "EnchantedElkhound", '2023-03-01 21:37:32'),
(768, 224, "RadiantRat", '2023-03-29 00:28:00'),
(769, 205, "ElectricEchidna", '2023-02-22 09:35:52'),
(773, 196, "LunarLemming", '2023-02-06 14:01:00'),
(774, 191, "VelvetVole", '2023-03-17 13:08:56'),
(790, 172, "FieryFrigatebird", '2023-02-14 07:58:59'),
(792, 161, "OceanicOcelot", '2023-03-12 02:07:39'),
(796, 159, "EnigmaticElk", '2023-01-10 00:57:40'),
(801, 119, "CrimsonCuckoo", '2023-03-27 12:27:39'),
(804, 105, "JadeJay", '2023-02-24 23:51:46'),
(809, 98, "MysticMole", '2023-03-29 17:52:20'),
(810, 92, "GalacticGorilla", '2023-02-23 19:27:42'),
(837, 72, "RadiantRhino", '2023-02-03 22:46:19'),
(870, 56, "SilverSwan", '2023-01-31 17:38:26'),
(882, 54, "CelestialCentipede", '2023-02-05 15:21:58'),
(901, 50, "CosmicChinchilla", '2023-03-18 01:14:57'),
(902, 40, "EnchantedEmperor", '2023-02-22 12:03:49'),
(907, 31, "FieryFlamingo", '2023-01-10 19:13:15'),
(910, 16, "StarryScorpion", '2023-02-21 10:30:57'),
(940, 15, "EmeraldEagle", '2023-04-03 23:14:09'),
(981, 8, "MysticMosquito", '2023-03-25 07:13:02'),
(993, 993, "ElectricEagleRay", '2023-02-05 03:03:57');
