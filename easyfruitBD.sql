-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-06-2022 a las 13:33:01
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `easyfruit`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cart`
--

CREATE TABLE `cart` (
  `customerId` int(4) NOT NULL,
  `productId` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cart`
--

INSERT INTO `cart` (`customerId`, `productId`) VALUES
(2, 8),
(17, 111),
(17, 112),
(17, 113);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `customer`
--

CREATE TABLE `customer` (
  `id` int(3) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `email` varchar(40) NOT NULL,
  `phone` varchar(9) DEFAULT NULL,
  `passwd` varchar(300) NOT NULL,
  `zip` varchar(20) NOT NULL,
  `address` varchar(500) DEFAULT NULL,
  `seller` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `customer`
--

INSERT INTO `customer` (`id`, `name`, `email`, `phone`, `passwd`, `zip`, `address`, `seller`) VALUES
(2, 'Carla Galán', 'carla@gmail.es', '919909987', 'sha256$MnmBdXPcxdHlJka1$5e6dd898ab9bdf5607b073396aa7cca23d061cb40a2cd9ab88edf5967d6ba850', '54579', 'Ancha 15, Córdoba', 'si'),
(8, 'Antonio jose lopez', 'Jjj@hotmail.es', '918989999', 'sha256$MnmBdXPcxdHlJka1$5e6dd898ab9bdf5607b073396aa7cca23d061cb40a2cd9ab88edf5967d6ba850', '23411', 'Conde 14, Córdoba', 'no'),
(9, 'juan gomez', 'juan@hotmail.es', '690699677', 'sha256$jvlPCxtusTjfzqHQ$c69bf40fef256b196181e7d841745ede63e243bdc255bb84fb980131b220e1b1', '14660', 'Ancha 15, Córdoba', 'no'),
(12, 'Anaaaa', 'Ana@hotmail.es', '699799899', 'sha256$CUsnS8aoNBAZQ2dE$d510f56097ee0b3340aa16cf6a32e60df0647a1f4a548fed168a28005bbbae32', '14660', 'Ancha 15, Córdoba', 'no'),
(13, 'Ana Murrio', 'anamurrio@hotmail.es', '600677699', 'sha256$mncaAWVeWlpE068t$f66852322cd83bf32116d26c6f96d72068048e70e3c3e399268f6c62987836da', '11467', 'Ancha 15, Córdoba', 'si'),
(14, 'Jaime Jimenez', 'jaimeoficial@hotmail.es', '699677690', 'sha256$4Q0kfQiLIQtqxWMN$76a05f2b75a42e526209ecb0e80aaf486a52a05d9c00009303939c8fd3ce0a9f', '14551', 'Ancha 15, Córdoba', 'si'),
(17, 'Admin', 'admin@admin.es', '000000000', 'sha256$62hM1WU0cxupSLGW$9cdffbcef82cca44a9c5a7b648a45b0844a4c0a8e5f36305c8d0cfd865cc829b', 'fdfdfds,vmc,vmcv', 'C. Cristobal Andalucía 254', 'no'),
(18, 'Manuel', 'stickyamp@hotmail.com', '665434658', 'sha256$OAI51KwkTUyPB970$9c45d396ea1d506230db8a8867ac534a265ba5f7b58d0e874d0d5bce1e3c5933', '14660', 'Calle Ancha, 15', 'no');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orden`
--

CREATE TABLE `orden` (
  `id` int(4) NOT NULL,
  `order_date` date NOT NULL,
  `estimated_total` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `anotations` varchar(2000) NOT NULL,
  `times_ordered` int(4) NOT NULL,
  `deliverOptions` varchar(100) NOT NULL,
  `fCustomer` int(4) NOT NULL,
  `fStore` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `orden`
--

INSERT INTO `orden` (`id`, `order_date`, `estimated_total`, `status`, `anotations`, `times_ordered`, `deliverOptions`, `fCustomer`, `fStore`) VALUES
(70, '2022-05-15', '5.25', 'created', 'Estoy usando EasyFruit!', 1, 'deliverHome', 8, 2),
(71, '2022-05-15', '8', 'created', 'Gracias por el servicio', 1, 'deliverHome', 8, 4),
(72, '2022-05-15', '164', 'created', 'Comida familiar, urgente', 1, 'deliverHome', 8, 4),
(74, '2022-05-16', '28', 'sent', '', 2, 'takeStore', 8, 1),
(76, '2022-05-16', '50', 'created', 'hola', 2, 'takeStore', 8, 4),
(77, '2022-05-18', '2', 'created', '12', 1, 'deliverHome', 8, 2),
(78, '2022-05-18', '6.6000000000000005', 'created', 'grx', 2, 'deliverHome', 8, 2),
(79, '2022-05-18', '6.6000000000000005', 'created', 'grx', 3, 'takeStore', 8, 2),
(80, '2022-05-18', '28', 'ready', 'Gracias por el servicio', 3, 'takeStore', 8, 1),
(81, '2022-05-18', '82.5', 'created', 'muchas gracias', 4, 'takeStore', 8, 2),
(82, '2022-05-19', '11.2', 'closed', 'Gracias por las molestias', 1, 'deliverHome', 8, 1),
(83, '2022-05-22', '86.1', 'ready', 'Gracias', 1, 'takeStore', 8, 1),
(84, '2022-05-31', '56', 'created', 'Gracias', 1, 'takeStore', 8, 1),
(85, '2022-05-31', '147', 'created', 'Gracias', 1, 'takeStore', 8, 1),
(86, '2022-05-31', '18', 'created', 'Thanks', 1, 'deliverHome', 8, 1),
(87, '2022-05-31', '2', 'created', '', 1, 'takeStore', 8, 1),
(88, '2022-05-31', '5.6', 'created', 'Envío urgente por favor', 1, 'takeStore', 8, 1),
(89, '2022-05-31', '28', 'created', 'Gracias por la opción de repetir!', 4, 'takeStore', 8, 1),
(90, '2022-05-31', '28', 'created', 'Gracias EasyFruit!', 5, 'takeStore', 8, 1),
(91, '2022-05-31', '28', 'created', 'Llamar al teléfono', 6, 'takeStore', 8, 1),
(92, '2022-05-31', '82.5', 'created', 'Gracias por las zanahorias', 5, 'takeStore', 8, 2),
(93, '2022-05-31', '18', 'created', 'Gracias!!', 2, 'deliverHome', 8, 1),
(94, '2022-05-31', '82.5', 'created', 'Envío a la oficina', 6, 'takeStore', 8, 2),
(95, '2022-06-07', '28', 'created', 'Muchas gracias', 7, 'takeStore', 8, 1),
(96, '2022-06-07', '28', 'created', 'Enviar al trabajo', 8, 'takeStore', 8, 1),
(97, '2022-06-07', '28', 'created', 'Mandar la semana que viene, no estoy en casa', 1, 'takeStore', 8, 1),
(98, '2022-06-08', '28', 'created', '', 9, 'takeStore', 8, 1),
(99, '2022-06-08', '13.260000000000002', 'created', 'Gracias', 1, 'deliverHome', 8, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenitem`
--

CREATE TABLE `ordenitem` (
  `ordenId` int(4) NOT NULL,
  `productId` int(4) NOT NULL,
  `methodSelected` varchar(70) NOT NULL,
  `unitsToBuy` varchar(70) NOT NULL,
  `estimated_price` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ordenitem`
--

INSERT INTO `ordenitem` (`ordenId`, `productId`, `methodSelected`, `unitsToBuy`, `estimated_price`) VALUES
(70, 115, 'pieces', '3', '2.4899999999999998'),
(70, 116, 'kg', '1', '1'),
(70, 117, 'pieces', '8', '1.76'),
(71, 100, 'kg', '', '0'),
(71, 104, 'kg', '2', '2'),
(71, 106, 'kg', '2', '6'),
(72, 100, 'kg', '20', '140'),
(72, 104, 'kg', '10', '10'),
(72, 105, 'kg', '2', '14'),
(74, 110, 'kg', '2', '14'),
(74, 111, 'kg', '1', '7'),
(74, 112, 'kg', '1', '1'),
(74, 113, 'kg', '3', '6'),
(76, 106, 'kg', '50', '50'),
(77, 116, 'kg', '2', '2'),
(78, 116, 'pack', '2', '6.6000000000000005'),
(79, 116, 'pack', '2', '6.6000000000000005'),
(80, 110, 'kg', '2', '14'),
(80, 111, 'kg', '1', '7'),
(80, 112, 'kg', '1', '1'),
(80, 113, 'kg', '3', '6'),
(81, 116, 'pack', '25', '82.5'),
(82, 110, 'pack', '4', '11.2'),
(83, 110, 'kg', '11', '77'),
(83, 111, 'pack', '2', '9.1'),
(84, 110, 'pack', '20', '56'),
(85, 110, 'kg', '20', '140'),
(85, 111, 'kg', '1', '7'),
(86, 111, 'kg', '2', '14'),
(86, 113, 'kg', '2', '4'),
(87, 112, 'kg', '2', '2'),
(88, 110, 'pack', '2', '5.6'),
(89, 110, 'kg', '2', '14'),
(89, 111, 'kg', '1', '7'),
(89, 112, 'kg', '1', '1'),
(89, 113, 'kg', '3', '6'),
(90, 110, 'kg', '2', '14'),
(90, 111, 'kg', '1', '7'),
(90, 112, 'kg', '1', '1'),
(90, 113, 'kg', '3', '6'),
(91, 110, 'kg', '2', '14'),
(91, 111, 'kg', '1', '7'),
(91, 112, 'kg', '1', '1'),
(91, 113, 'kg', '3', '6'),
(92, 116, 'pack', '25', '82.5'),
(93, 111, 'kg', '2', '14'),
(93, 113, 'kg', '2', '4'),
(94, 116, 'pack', '25', '82.5'),
(95, 110, 'kg', '2', '14'),
(95, 111, 'kg', '1', '7'),
(95, 112, 'kg', '1', '1'),
(95, 113, 'kg', '3', '6'),
(96, 110, 'kg', '2', '14'),
(96, 111, 'kg', '1', '7'),
(96, 112, 'kg', '1', '1'),
(96, 113, 'kg', '3', '6'),
(97, 110, 'kg', '4', '28'),
(98, 110, 'kg', '2', '14'),
(98, 111, 'kg', '1', '7'),
(98, 112, 'kg', '1', '1'),
(98, 113, 'kg', '3', '6'),
(99, 115, 'pieces', '6', '4.9799999999999995'),
(99, 116, 'pack', '3', '6.300000000000001'),
(99, 117, 'pack', '2', '1.98');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product`
--

CREATE TABLE `product` (
  `id` int(3) NOT NULL,
  `name` varchar(100) NOT NULL,
  `product_img` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `price_per_kg` int(30) NOT NULL,
  `price_per_unit` varchar(70) NOT NULL,
  `price_per_pack` varchar(70) NOT NULL,
  `packQuantity` varchar(70) DEFAULT NULL,
  `description` varchar(5000) NOT NULL,
  `methodsAllowed` varchar(70) NOT NULL,
  `fCategory` int(3) NOT NULL,
  `fStore` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `product`
--

INSERT INTO `product` (`id`, `name`, `product_img`, `price_per_kg`, `price_per_unit`, `price_per_pack`, `packQuantity`, `description`, `methodsAllowed`, `fCategory`, `fStore`) VALUES
(100, 'Arándano exótico', 'http://localhost:3000/api/v1/product/get_image/100_product', 7, '0', '0', '0', 'Arándano silvestre de la selva negra.', 'kg;', 2, 4),
(104, 'Sandía', 'http://localhost:3000/api/v1/product/get_image/104_product', 1, '3', '0', '0', 'Sandía de la huerta de almería. Gran sabor y textura.', 'kg;pieces;', 2, 4),
(105, 'Cereza grande', 'http://localhost:3000/api/v1/product/get_image/105_product', 7, '0', '0', '0', 'Cerezas grandes sin hueso.', 'kg;', 2, 4),
(106, 'Uvas', 'http://localhost:3000/api/v1/product/get_image/106_product', 3, '0', '1.7', '30', 'Uvas ácidas y sin pepitas.', 'kg;pack', 2, 4),
(108, 'Kiwi dulce', 'http://localhost:3000/api/v1/product/get_image/108_product', 4, '0.69', '2.37', '6', 'Kiwi dulce proveniente de Granada.', 'kg;pieces;pack', 2, 4),
(109, 'Naranja fresca', 'http://localhost:3000/api/v1/product/get_image/109_product', 1, '0.2', '3', '15', 'Producto nacional de calidad. Naranja valenciana.', 'kg;pieces;pack', 2, 4),
(110, 'Almendra natural', 'http://localhost:3000/api/v1/product/get_image/110_product', 7, '0', '2.8', '50', 'Producto nacional de calidad. Sin conservantes ni añadidos.', 'kg;pack', 5, 1),
(111, 'Nuez natural', 'http://localhost:3000/api/v1/product/get_image/111_product', 7, '0', '4.55', '30', 'Producto importado. Nuez italiana gourmet.', 'kg;pack', 5, 1),
(112, 'Lentejas ', 'http://localhost:3000/api/v1/product/get_image/112_product', 1, '0', '0', '0', 'Producto natural vendido por kilos.', 'kg;', 6, 1),
(113, 'Garbanzos', 'http://localhost:3000/api/v1/product/get_image/113_product', 2, '0', '0', '0', 'Garbanzo español', 'kg;', 6, 1),
(114, 'Ajo', 'http://localhost:3000/api/v1/product/get_image/114_product', 0, '0.27', '2.65', '20', 'Ajo importado', 'pieces;pack', 4, 2),
(115, 'Coliflor', 'http://localhost:3000/api/v1/product/get_image/115_product', 0, '0.83', '1.99', '4', 'Coliflor recién salida de la huerta.', 'pieces;pack', 4, 2),
(116, 'Zanahoria', 'http://localhost:3000/api/v1/product/get_image/116_product', 1, '0.33', '2.1', '10', 'Zanahoria verde y sabrosa', 'kg;pieces;pack', 4, 2),
(117, 'Cebolla', 'http://localhost:3000/api/v1/product/get_image/117_product', 0, '0.22', '0.99', '6', 'Cebolla fuerte', 'pieces;pack', 4, 2),
(118, 'Espinaca', 'http://localhost:3000/api/v1/product/get_image/118_product', 3, '0', '0', '0', 'Espinaca de la huerta de Almería', 'kg;', 4, 2),
(119, 'Espárragos', 'http://localhost:3000/api/v1/product/get_image/119_product', 4, '0,35', '3', '10', 'Espárragos naturales, recien cortados.', 'kg;pieces;pack', 4, 2),
(120, 'Brócoli', 'http://localhost:3000/api/v1/product/get_image/120_product', 3, '0', '2.45', '12', 'Brócoli al peso.', 'kg;pack', 4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productcategory`
--

CREATE TABLE `productcategory` (
  `id` int(3) NOT NULL,
  `name` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `productcategory`
--

INSERT INTO `productcategory` (`id`, `name`) VALUES
(1, 'General'),
(2, 'Fruta'),
(4, 'Verdura'),
(5, 'Frutos secos'),
(6, 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `store`
--

CREATE TABLE `store` (
  `id` int(3) NOT NULL,
  `address` varchar(90) NOT NULL,
  `comercial_logo` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(60) NOT NULL,
  `phone` varchar(60) NOT NULL,
  `storemanager` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `store`
--

INSERT INTO `store` (`id`, `address`, `comercial_logo`, `name`, `phone`, `storemanager`) VALUES
(1, 'Calle Palmar Nº27,  Portal 1, Córdoba', 'http://localhost:3000/api/v1/store/get_image/1_store', 'Productos Carla', '699678609', 'carla@gmail.es'),
(2, '1th South West, England', 'http://localhost:3000/api/v1/store/get_image/2_store', 'VerduShop', '87 955 344 122', 'anamurrio@hotmail.es'),
(4, 'Avd. Victoria, Nº103, Granada', 'http://localhost:3000/api/v1/store/get_image/4_store', 'Oficial Fruit', '655623698', 'jaimeoficial@hotmail.es');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`customerId`,`productId`);

--
-- Indices de la tabla `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `orden`
--
ALTER TABLE `orden`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ordencustomer_fk` (`fCustomer`),
  ADD KEY `ordenstore` (`fStore`);

--
-- Indices de la tabla `ordenitem`
--
ALTER TABLE `ordenitem`
  ADD PRIMARY KEY (`ordenId`,`productId`),
  ADD KEY `ordenitemproduct_fk` (`productId`);

--
-- Indices de la tabla `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fCategory` (`fCategory`);

--
-- Indices de la tabla `productcategory`
--
ALTER TABLE `productcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `orden`
--
ALTER TABLE `orden`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT de la tabla `product`
--
ALTER TABLE `product`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT de la tabla `productcategory`
--
ALTER TABLE `productcategory`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `store`
--
ALTER TABLE `store`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `orden`
--
ALTER TABLE `orden`
  ADD CONSTRAINT `ordencustomer_fk` FOREIGN KEY (`fCustomer`) REFERENCES `customer` (`id`),
  ADD CONSTRAINT `ordenstore` FOREIGN KEY (`fStore`) REFERENCES `store` (`id`);

--
-- Filtros para la tabla `ordenitem`
--
ALTER TABLE `ordenitem`
  ADD CONSTRAINT `ordenitemorden_fk` FOREIGN KEY (`ordenId`) REFERENCES `orden` (`id`),
  ADD CONSTRAINT `ordenitemproduct_fk` FOREIGN KEY (`productId`) REFERENCES `product` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
