DROP TABLE IF EXISTS Follows;

CREATE TABLE IF NOT EXISTS Follows(
id INT AUTO_INCREMENT,
follower VARCHAR(255) NOT NULL,
followed VARCHAR(255) NOT NULL,
timestamp DATETIME NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY (follower) REFERENCES Users(username) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (followed) REFERENCES Users(username) ON UPDATE CASCADE ON DELETE CASCADE
);

DELIMITER //
CREATE TRIGGER CreateFollowNotification
    AFTER INSERT ON Follows
    FOR EACH ROW
    BEGIN
        INSERT INTO Notifications (id, type, status) VALUES (NEW.id, 'follow', 'unread');
		END; //
DELIMITER ;

INSERT INTO Follows (id, follower, followed, timestamp)
VALUES
(1, "OceanicOctopus", "CelestialCaterpillar", '2023-01-10 00:42:50'),
(2, "EmeraldDragonfly", "MysticMermaid", '2023-03-06 11:12:27'),
(3, "BlissfulGnome", "CosmicCoyote", '2023-01-05 21:51:19'),
(4, "SapphireJazz", "CelestialSiren", '2023-02-21 18:48:52'),
(5, "MysticWombat", "SapphireStork", '2023-02-28 05:49:14'),
(6, "ElectricPenguin", "EnchantedEagle", '2023-02-11 05:07:28'),
(7, "CosmicChameleon", "RadiantRabbit", '2023-02-25 22:00:45'),
(8, "VelvetPhoenix", "LunarLion", '2023-04-07 06:11:39'),
(9, "RadiantLynx", "VelvetVixen", '2023-02-20 19:22:58'),
(10, "LunarSphinx", "FieryFeline", '2023-03-24 09:45:10'),
(11, "GalacticSailor", "ElectricElephant", '2023-02-01 00:05:33'),
(12, "CrimsonCobra", "OceanicOstrich", '2023-02-15 13:36:10'),
(13, "CelestialRaven", "EnigmaticEmu", '2023-02-24 11:38:35'),
(14, "SilverStallion", "CrimsonCrocodile", '2023-03-18 11:49:16'),
(15, "EnigmaticKraken", "JadeJellyfish", '2023-01-01 11:01:55'),
(16, "EmeraldDragonfly", "MysticMongoose", '2023-02-04 01:19:26'),
(17, "MysticMoose", "GalacticGazelle", '2023-01-14 01:59:39'),
(18, "FieryFalcon", "RadiantRoadrunner", '2023-01-29 23:37:57'),
(19, "OceanicOctopus", "SilverSquirrel", '2023-01-08 12:23:47'),
(20, "CrimsonCheetah", "CelestialCrane", '2023-01-12 12:33:20'),
(21, "CosmicCactus", "CosmicCamel", '2023-03-29 06:43:54'),
(22, "EnchantedElk", "EnchantedEchidna", '2023-02-25 13:11:13'),
(23, "RadiantRaccoon", "FieryFerret", '2023-01-22 02:14:56'),
(24, "JadeJaguar", "StarryShark", '2023-02-12 05:16:09'),
(25, "StarrySwan", "EmeraldElk", '2023-03-01 18:13:18'),
(26, "ElectricEagle", "MysticManta", '2023-04-02 19:43:16'),
(27, "EmeraldDragonfly", "RadiantRaven", '2023-03-28 16:13:22'),
(28, "CosmicChameleon", "CosmicCobra", '2023-04-02 05:52:08'),
(29, "FieryFox", "SapphireSeahorse", '2023-02-23 07:22:48'),
(30, "BlissfulGnome", "MysticMonkey", '2023-03-25 04:31:31'),
(31, "SapphireJazz", "EnchantedEel", '2023-01-25 21:51:07'),
(32, "MysticWombat", "ElectricElk", '2023-02-16 20:15:21'),
(33, "ElectricPenguin", "LunarLlama", '2023-01-03 22:03:51'),
(34, "VelvetPhoenix", "VelvetVampire", '2023-03-23 17:16:43'),
(35, "RadiantLynx", "FieryFawn", '2023-04-03 04:18:24'),
(36, "LunarSphinx", "OceanicOtter", '2023-02-08 09:03:41'),
(37, "GalacticSailor", "EnigmaticEagle", '2023-03-09 16:37:54'),
(38, "CrimsonCobra", "CrimsonCormorant", '2023-03-17 04:24:27'),
(39, "CelestialRaven", "JadeJester", '2023-01-08 16:24:50'),
(40, "SilverStallion", "MysticMarmot", '2023-01-13 21:31:02'),
(41, "EnigmaticKraken", "GalacticGiraffe", '2023-01-02 08:14:14'),
(42, "MysticMoose", "RadiantRaccoon", '2023-04-06 22:48:34'),
(43, "FieryFalcon", "SilverSnake", '2023-03-03 07:06:33'),
(44, "CrimsonCheetah", "CosmicCivet", '2023-01-17 21:42:50'),
(45, "CosmicCactus", "EnchantedEagle", '2023-03-18 11:41:38'),
(46, "EnchantedElk", "FieryFalconer", '2023-01-02 03:42:19'),
(47, "RadiantRaccoon", "StarryStingray", '2023-02-09 05:20:47'),
(48, "JadeJaguar", "EmeraldEchidna", '2023-01-06 04:20:50'),
(49, "StarrySwan", "MysticMoth", '2023-01-09 22:44:45'),
(50, "ElectricEagle", "ElectricElephant", '2023-04-02 16:39:52'),
(51, "EmeraldDragonfly", "CosmicCougar", '2023-03-30 09:56:16'),
(52, "FieryFox", "SapphireSparrow", '2023-01-20 21:35:18'),
(53, "BlissfulGnome", "MysticMandrill", '2023-03-02 07:07:51'),
(54, "SapphireJazz", "EnchantedElkhound", '2023-04-07 14:18:26'),
(55, "MysticWombat", "RadiantRat", '2023-03-09 02:16:53'),
(56, "ElectricPenguin", "ElectricEchidna", '2023-02-10 15:10:43'),
(57, "CosmicChameleon", "LunarLemming", '2023-01-07 09:34:42'),
(58, "VelvetPhoenix", "VelvetVole", '2023-02-17 23:11:05'),
(59, "RadiantLynx", "FieryFrigatebird", '2023-01-01 16:43:13'),
(60, "LunarSphinx", "OceanicOcelot", '2023-04-01 15:02:20'),
(61, "GalacticSailor", "EnigmaticElk", '2023-03-05 11:22:22'),
(62, "CrimsonCobra", "CrimsonCuckoo", '2023-01-22 02:32:41'),
(63, "CelestialRaven", "JadeJay", '2023-02-13 03:12:57'),
(64, "SilverStallion", "MysticMole", '2023-01-10 20:24:17'),
(65, "EnigmaticKraken", "GalacticGorilla", '2023-03-29 18:22:20'),
(66, "MysticMoose", "RadiantRhino", '2023-01-04 11:52:26'),
(67, "FieryFalcon", "SilverSwan", '2023-03-19 22:14:22'),
(68, "OceanicOctopus", "CelestialCentipede", '2023-04-01 08:11:04'),
(69, "CrimsonCheetah", "CosmicChinchilla", '2023-02-21 23:17:40'),
(70, "CosmicCactus", "EnchantedEmperor", '2023-03-01 20:10:56'),
(71, "EnchantedElk", "FieryFlamingo", '2023-03-30 14:00:46'),
(72, "RadiantRaccoon", "StarryScorpion", '2023-01-24 12:11:30'),
(73, "JadeJaguar", "EmeraldEagle", '2023-01-28 11:07:06'),
(74, "StarrySwan", "MysticMosquito", '2023-03-07 16:35:35'),
(75, "ElectricEagle", "ElectricEagleRay", '2023-03-20 06:41:02'),
(76, "CelestialCentipede", "BlissfulGnome", '2023-03-20 04:34:56'),
(77, "FieryFox", "SapphireJazz", '2023-01-10 08:23:59'),
(78, "SapphireSparrow", "MysticWombat", '2023-01-27 21:14:53'),
(79, "MysticMandrill", "ElectricPenguin", '2023-03-26 18:12:32'),
(80, "EnchantedElkhound", "CosmicChameleon", '2023-01-25 20:28:16'),
(81, "RadiantRat", "VelvetPhoenix", '2023-03-14 01:04:57'),
(82, "ElectricEchidna", "RadiantLynx", '2023-01-29 21:25:12'),
(83, "LunarLemming", "LunarSphinx", '2023-02-18 12:34:39'),
(84, "VelvetVole", "GalacticSailor", '2023-03-04 10:34:01'),
(85, "FieryFrigatebird", "CrimsonCobra", '2023-03-25 01:57:33'),
(86, "OceanicOcelot", "CelestialRaven", '2023-03-03 21:03:53'),
(87, "EnigmaticElk", "SilverStallion", '2023-04-06 05:58:41'),
(88, "CrimsonCuckoo", "EnigmaticKraken", '2023-02-01 05:21:12'),
(89, "JadeJay", "EmeraldDragonfly", '2023-03-17 02:06:08'),
(90, "MysticMole", "MysticMoose", '2023-01-09 19:49:55'),
(91, "GalacticGorilla", "FieryFalcon", '2023-01-08 18:12:27'),
(92, "RadiantRhino", "OceanicOctopus", '2023-01-02 23:35:07'),
(93, "SilverSwan", "CrimsonCheetah", '2023-02-15 22:35:40'),
(94, "CelestialCentipede", "CosmicCactus", '2023-02-05 00:35:40'),
(95, "CosmicChinchilla", "EnchantedElk", '2023-02-04 19:57:29'),
(96, "EnchantedEmperor", "RadiantRaccoon", '2023-01-31 00:27:52'),
(97, "FieryFlamingo", "JadeJaguar", '2023-02-15 10:24:37'),
(98, "StarryScorpion", "StarrySwan", '2023-03-19 22:01:21'),
(99, "EmeraldEagle", "ElectricEagle", '2023-01-18 07:20:52'),
(100, "MysticMosquito", "FieryFox", '2023-04-01 02:00:51');