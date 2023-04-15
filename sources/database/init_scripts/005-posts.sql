DROP TABLE IF EXISTS Posts;

CREATE TABLE IF NOT EXISTS Posts(
id INT AUTO_INCREMENT,
author VARCHAR(255) NOT NULL,
body TEXT NOT NULL,
police VARCHAR(255) NOT NULL,
timestamp DATETIME NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(author) REFERENCES Users(username) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Posts (id, author, body, police, timestamp)
VALUES
(314, "BlissfulGnome", "Le bonheur, c'est de continuer à désirer ce que l'on possède.", "Arial", '2023-02-28 16:22:08'),
(540, "SapphireJazz", "La vie, c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre.", "Times New Roman", '2023-02-08 14:17:15'),
(159, "MysticWombat", "Le temps est un grand maître, dit-on. Le malheur est qu'il tue ses élèves.", "Helvetica", '2023-03-07 22:25:11'),
(837, "ElectricPenguin", "La vie est une fleur dont l'amour est le miel.", "Courier New", '2023-02-01 17:09:39'),
(420, "CosmicChameleon", "L'important n'est pas ce que l'on a, mais ce que l'on donne.", "Verdana", '2023-01-01 17:03:10'),
(644, "VelvetPhoenix", "Il n'y a pas de réussite facile ni d'échecs définitifs.", "Georgia", '2023-01-07 05:15:48'),
(731, "RadiantLynx", "La simplicité est la sophistication suprême.", "Palatino", '2023-01-28 03:11:38'),
(724, "LunarSphinx", "Le talent, c'est d'avoir envie.", "Comic Sans", '2023-01-26 17:49:02'),
(396, "GalacticSailor", "La vie, c'est comme une pièce de théâtre : ce qui compte, ce n'est pas qu'elle dure longtemps, c'est qu'elle soit bien jouée.", "Impact", '2023-03-01 06:39:41'),
(224, "CrimsonCobra", "Le plus grand risque dans la vie, c'est de ne pas en prendre.", "Garamond", '2023-01-20 11:50:40'),
(993, "CelestialRaven", "Le vrai bonheur ne dépend d'aucun être, d'aucun objet extérieur. Il ne dépend que de nous.", "Century Gothic", '2023-01-11 03:14:05'),
(105, "SilverStallion", "La beauté est dans les yeux de celui qui regarde.", "Futura", '2023-02-27 08:51:33'),
(298, "EnigmaticKraken", "La persévérance est la clé de la réussite.", "Calibri", '2023-03-05 09:09:33'),
(796, "EmeraldDragonfly", "Tout ce qui ne me tue pas me rend plus fort.", "Lucida Sans", '2023-01-17 03:10:47'),
(468, "MysticMoose", "Il n'y a pas de plus grande richesse que la paix intérieure.", "Copperplate", '2023-03-01 22:42:16'),
(119, "FieryFalcon", "Le bonheur, c'est de pouvoir s'émerveiller encore et toujours.", "Tahoma", '2023-02-21 16:37:49'),
(691, "OceanicOctopus", "Il faut viser la lune, parce qu'au moins, si vous échouez, vous finissez dans les étoiles.", "Franklin Gothic", '2023-01-09 17:37:03'),
(637, "CrimsonCheetah", "Le vrai voyage de découverte ne consiste pas à chercher de nouveaux paysages, mais à avoir de nouveaux yeux.", "Baskerville", '2023-01-10 21:03:56'),
(277, "CosmicCactus", "La vie est un mystère qu'il faut vivre, et non un problème à résoudre.", "Book Antiqua", '2023-01-22 12:06:26'),
(191, "EnchantedElk", "La patience est l'art d'espérer.", "Rockwell", '2023-02-28 09:43:09'),
(536, "RadiantRaccoon", "Le plus grand secret pour le bonheur, c'est d'être bien avec soi-même.", "Brush Script", '2023-02-01 11:29:08'),
(16, "JadeJaguar", "L'échec est le fondement de la réussite.", "Eurostile", '2023-03-28 01:56:04'),
(444, "StarrySwan", "Rien n'est permanent, sauf le changement.", "Optima", '2023-01-01 01:03:32'),
(72, "ElectricEagle", "La joie de vivre est une émotion contagieuse.", "Segoe UI", '2023-01-13 16:27:42'),
(769, "FieryFox", "La vie est une aventure audacieuse ou rien du tout.", "Trebuchet MS", '2023-02-23 22:24:17'),
(172, "SapphireJazz", "La créativité est la capacité de voir les choses sous un angle différent et de les transformer en quelque chose de nouveau.", 'Times New Roman', '2023-02-10 07:32:30'),
(907, "BlissfulGnome", "Le silence est une oasis de paix au milieu du tumulte du monde.", 'Arial', '2023-01-29 20:08:51'),
(616, "MysticWombat", "La confiance en soi est la clé pour accomplir de grandes choses dans la vie.", 'Helvetica', '2023-03-14 19:14:07'),
(280, "ElectricPenguin", "Le courage, c'est d'aller de l'avant malgré la peur et les doutes qui nous habitent.", 'Courier New', '2023-02-23 14:42:34'),
(882, "CosmicChameleon", "La gratitude est un baume pour l'âme qui nous permet de voir la beauté dans les petites choses de la vie.", 'Verdana', '2023-03-11 16:53:11'),
(56, "VelvetPhoenix", "Le bonheur n'est pas une destination, mais un état d'esprit que l'on peut cultiver chaque jour.", 'Georgia', '2023-03-11 00:14:04'),
(659, "RadiantLynx", "Le respect est la base de toute relation saine et épanouissante.", 'Palatino', '2023-03-24 14:20:30'),
(792, "LunarSphinx", "La vie est une aventure à explorer avec curiosité et émerveillement.", 'Comic Sans', '2023-03-30 00:00:42'),
(543, "GalacticSailor", "La bienveillance est une force qui peut changer le monde, une personne à la fois.", 'Impact', '2023-03-25 19:38:18'),
(388, "CrimsonCobra", "La sagesse, c'est de savoir accepter ce que l'on ne peut pas changer et de changer ce que l'on peut.", 'Garamond', '2023-03-11 16:17:12'),
(686, "CelestialRaven", "La vie est une danse, il suffit de se laisser porter par la musique.", 'Century Gothic', '2023-02-04 16:51:14'),
(98, "SilverStallion", "L'amitié est un trésor précieux qui illumine notre chemin de vie.", 'Futura', '2023-03-09 23:23:21'),
(498, "EnigmaticKraken", "Le sourire est le langage universel de l'amour et de la joie.", 'Calibri', '2023-01-29 23:08:41'),
(40, "EmeraldDragonfly", "La véritable beauté est celle qui émane de l'intérieur, de l'âme et du cœur.", 'Lucida Sans', '2023-02-06 18:15:13'),
(325, "MysticMoose", "L'espoir est la lumière qui brille dans l'obscurité et qui nous guide vers un avenir meilleur.", 'Copperplate', '2023-03-16 16:41:32'),
(870, "FieryFalcon", "La vie est une œuvre d'art que l'on crée chaque jour avec les couleurs de notre imagination.", 'Tahoma', '2023-02-28 16:49:25'),
(15, "OceanicOctopus", "Le bonheur, c'est de vivre en harmonie avec soi-même et avec les autres.", 'Franklin Gothic', '2023-01-28 01:07:49'),
(412, "CrimsonCheetah", "La générosité est une fleur qui ne cesse de fleurir lorsqu'on la cultive avec amour.", 'Baskerville', '2023-02-01 01:28:57'),
(732, "CosmicCactus", "La patience est la vertu qui nous permet d'atteindre nos objectifs, même lorsque le chemin est difficile.", 'Book Antiqua', '2023-02-26 20:35:36'),
(595, "EnchantedElk", "Le rire est un remède pour l'âme qui nous permet de faire face aux difficultés de la vie.", 'Rockwell', '2023-01-11 15:25:58'),
(801, "RadiantRaccoon", "Le pardon est la clé pour libérer notre cœur des chaînes du ressentiment et de la colère.", 'Brush Script', '2023-02-27 14:14:09'),
(295, "JadeJaguar", "La vie est un mystère à découvrir, une aventure à vivre avec passion et enthousiasme.", 'Eurostile', '2023-01-13 07:55:04'),
(638, "StarrySwan", "La curiosité est la force qui nous pousse à explorer l'inconnu et à découvrir de nouveaux horizons.", 'Optima', '2023-02-12 18:43:20'),
(810, "ElectricEagle", "La persévérance est la qualité qui nous permet de tenir bon face aux obstacles et aux défis de la vie.", 'Segoe UI', '2023-03-11 10:54:15'),
(617, "FieryFox", "La vie est un cadeau précieux, il faut l'apprécier à sa juste valeur et en prendre soin chaque jour.", 'Trebuchet MS', '2023-01-30 02:37:16'),
(431, "CosmicCougar", "Je ne suis pas en surpoids, je suis juste trop petite pour ma taille.", 'Arial', '2023-04-03 17:21:06'),
(679, "SapphireSparrow", "Je déteste la réalité, mais ça reste encore le meilleur endroit pour trouver un bon steak.", 'Times New Roman', '2023-03-05 07:11:28'),
(910, "MysticMandrill", "Les régimes, c'est comme les prisons : vous les quittez un jour ou l'autre.", 'Helvetica', '2023-01-12 11:14:11'),
(377, "EnchantedElkhound", "Je suis un intellectuel. J'aime tout ce qui est intellectuel, comme le hockey sur glace.", 'Courier New', '2023-01-13 02:06:33'),
(743, "RadiantRat", "Je suis tellement maladroit que je pourrais tomber dans une baignoire vide.", 'Verdana', '2023-01-17 14:01:47'),
(573, "ElectricEchidna", "Je suis allergique aux fausses promesses et aux chats.", 'Georgia', '2023-02-26 15:35:35'),
(382, "LunarLemming", "Le matin, je me lève tôt pour profiter de ma journée de procrastination.", 'Palatino', '2023-03-16 06:13:24'),
(901, "VelvetVole", "Je ne bois jamais d'eau, ça rouille les tuyaux.", 'Comic Sans', '2023-03-07 15:24:01'),
(458, "FieryFrigatebird", "Je suis le dernier de ma race. Et puis, j'ai raté le train.", 'Impact', '2023-02-16 07:32:30'),
(737, "OceanicOcelot", "Je suis né tellement loin dans le futur que les insultes des années 90 me font rire.", 'Garamond', '2023-03-20 04:26:38'),
(594, "EnigmaticElk", "J'ai arrêté de boire, mais seulement lorsque j'ai dormi.", 'Century Gothic', '2023-02-11 01:58:23'),
(718, "CrimsonCuckoo", "Je suis tellement vieux que j'ai l'impression d'être à l'origine de la préhistoire.", 'Futura', '2023-03-24 02:49:30'),
(54, "JadeJay", "Le sport, c'est bon pour la santé. J'ai arrêté dès que j'ai été en bonne santé.", 'Calibri', '2023-02-14 23:20:41'),
(902, "MysticMole", "Je suis allergique aux piqûres de moustique. Je pense que je suis la seule personne à qui les moustiques ne laissent pas tranquille.", 'Lucida Sans', '2023-02-24 01:03:32'),
(31, "GalacticGorilla", "Je suis tellement doué en multitâches que je peux me tromper en même temps sur plusieurs choses.", 'Copperplate', '2023-01-06 15:55:41'),
(313, "RadiantRhino", "Je suis végétarien depuis longtemps. Non pas parce que j'aime les animaux, mais parce que je déteste les légumes.", 'Tahoma', '2023-04-01 21:38:41'),
(205, "SilverSwan", "Je suis prêt à tout, sauf à sortir de ma zone de confort.", 'Franklin Gothic', '2023-01-10 06:10:35'),
(759, "CelestialCentipede", "Je suis assez intelligent pour réaliser que je suis assez idiot.", 'Baskerville', '2023-03-08 04:34:11'),
(725, "CosmicChinchilla", "Je suis un éternel optimiste. Je crois toujours que la dernière goutte de vin sera la bonne.", 'Book Antiqua', '2023-04-06 04:55:44'),
(611, "EnchantedEmperor", "Je suis incapable de répondre à cette question. Je suis trop occupé à m'inquiéter pour rien.", 'Rockwell', '2023-03-16 12:03:39'),
(92, "FieryFlamingo", "Je suis un grand amateur de musique classique. Surtout celle que personne ne connaît.", 'Brush Script', '2023-02-24 17:27:53'),
(774, "StarryScorpion", "Je suis contre la discrimination. Je déteste tout le monde également.", 'Eurostile', '2023-02-17 13:11:14'),
(981, "EmeraldEagle", "Je suis une personne très ouverte d'esprit. Si vous êtes d'accord avec moi, alors vous avez raison.", 'Optima', '2023-03-25 08:12:49'),
(726, "MysticMosquito", "Je suis allergique aux retards. Je suis toujours en avance ou en retard, jamais à l'heure.", 'Segoe UI', '2023-01-11 05:20:31'),
(276, "ElectricEagleRay", "Je suis un pessimiste heureux. Je suis toujours prêt à être déçu, mais rarement surpris.", 'Trebuchet MS', '2023-02-12 23:44:27'),
(773, "CosmicCougar", "Le silence est d'or, sauf quand il faut répondre à une question.", 'Arial', '2023-02-10 02:23:53'),
(196, "SapphireSparrow", "La vie est comme une boîte de chocolats, on ne sait jamais sur quoi on va tomber.", 'Times New Roman', '2023-02-26 02:16:15'),
(267, "MysticMandrill", "Le temps guérit toutes les blessures, sauf celles que l'amour inflige.", 'Helvetica', '2023-02-01 11:44:20'),
(161, "EnchantedElkhound", "Le rire est une thérapie gratuite. Ne pas en profiter serait une folie.", 'Courier New', '2023-01-05 19:12:56'),
(239, "RadiantRat", "Le plus dur n'est pas de tomber, c'est de se relever.", 'Verdana', '2023-03-27 23:14:12'),
(245, "ElectricEchidna", "L'ignorance n'est pas une excuse, c'est une opportunité d'apprendre.", 'Georgia', '2023-03-23 07:12:23'),
(768, "LunarLemming", "La seule façon de faire du bon travail est d'aimer ce que vous faites.", 'Palatino', '2023-02-07 02:47:12'),
(425, "VelvetVole", "La vie est un voyage, pas une destination.", 'Comic Sans', '2023-02-01 09:07:00'),
(8, "FieryFrigatebird", "L'amitié est la clé de voûte de la vie. Sans amis, la vie n'a pas de sens.", 'Impact', '2023-01-09 15:53:53'),
(410, "OceanicOcelot", "Le succès n'est pas final, l'échec n'est pas fatal : c'est le courage de continuer qui compte.", 'Garamond', '2023-03-20 03:36:26'),
(486, "EnigmaticElk", "Le vrai bonheur ne dépend d'aucun être, d'aucun objet extérieur. Il ne dépend que de nous-mêmes.", 'Century Gothic', '2023-01-02 23:02:51'),
(272, "CrimsonCuckoo", "La seule façon de faire du bon travail est d'aimer ce que vous faites.", 'Futura', '2023-01-30 17:09:18'),
(742, "JadeJay", "La beauté est dans les yeux de celui qui regarde.", 'Calibri', '2023-02-04 05:06:33'),
(804, "MysticMole", "La perfection n'est pas atteignable, mais si nous visons la perfection, nous pouvons atteindre l'excellence.", 'Lucida Sans', '2023-02-25 08:35:48'),
(525, "GalacticGorilla", "La vie est un jeu, jouez-le ; la vie est une aventure, osez-la.", 'Copperplate', '2023-02-03 04:49:09'),
(940, "RadiantRhino", "La seule limite à notre réalisation de demain sera nos doutes d'aujourd'hui.", 'Tahoma', '2023-03-31 06:07:29'),
(305, "SilverSwan", "Le plus grand risque dans la vie est de ne pas en prendre.", 'Franklin Gothic', '2023-02-21 18:54:16'),
(562, "CelestialCentipede", "Le bonheur n'est pas quelque chose de prêt à l'emploi. Il vient de vos propres actions.", 'Baskerville', '2023-02-26 14:23:22'),
(790, "CosmicChinchilla", "La vie est une roue qui tourne. Parfois, vous êtes en haut, parfois vous êtes en bas.", 'Book Antiqua', '2023-02-02 17:06:07'),
(485, "EnchantedEmperor", "La vie est un miroir et vous obtenez le reflet de ce que vous êtes.", 'Rockwell', '2023-01-24 02:41:54'),
(300, "FieryFlamingo", "Le changement est la loi de la vie. Ceux qui ne regardent que le passé ou le présent sont sûrs de manquer l'avenir.", 'Brush Script', '2023-02-14 17:28:37'),
(50, "StarryScorpion", "Le travail acharné est la clé de la réussite. Rien n'est facile, mais tout est possible avec de la persévérance.", 'Eurostile', '2023-02-28 13:24:08'),
(809, "EmeraldEagle", "La gratitude est la plus belle fleur qui jaillit de l'âme.", 'Optima', '2023-02-19 12:08:49'),
(717, "MysticMosquito", "Le monde est un livre, et ceux qui ne voyagent pas n'en lisent qu'une page.", 'Segoe UI', '2023-01-08 02:31:05'),
(658, "ElectricEagleRay", "La sagesse, c'est d'avoir des rêves suffisamment grands pour ne pas les perdre de vue lorsqu'on les poursuit.", 'Trebuchet MS', '2023-01-16 11:45:09');
