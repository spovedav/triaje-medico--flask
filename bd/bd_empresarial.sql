-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-12-2019 a las 05:32:22
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_empresarial`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admision`
--

CREATE TABLE `admision` (
  `cod_paciente` int(11) NOT NULL,
  `cod_agenda` int(11) NOT NULL,
  `cod_historial` int(11) DEFAULT NULL,
  `nombre1` varchar(50) DEFAULT NULL,
  `nombre2` varchar(50) DEFAULT NULL,
  `apellido1` varchar(50) DEFAULT NULL,
  `apellido2` varchar(50) DEFAULT NULL,
  `cedula` varchar(15) DEFAULT NULL,
  `fecha_nacimiento` varchar(11) DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `estado_civil` char(1) DEFAULT NULL,
  `domicilio` varchar(300) DEFAULT NULL,
  `telef_domicilio` varchar(10) DEFAULT NULL,
  `celular` varchar(10) DEFAULT NULL,
  `correo` varchar(200) DEFAULT NULL,
  `ADMISION` varchar(20) DEFAULT NULL,
  `fecha_ingreso` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agendar`
--

CREATE TABLE `agendar` (
  `cod_agenda` int(11) NOT NULL,
  `nombre1` varchar(50) DEFAULT NULL,
  `apellido1` varchar(50) DEFAULT NULL,
  `telf` varchar(10) DEFAULT NULL,
  `cod_doctor` int(11) DEFAULT NULL,
  `fecha_cita` varchar(11) DEFAULT NULL,
  `hora` varchar(5) DEFAULT NULL,
  `observacion` varchar(300) DEFAULT NULL,
  `confir` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `control_`
--

CREATE TABLE `control_` (
  `año` varchar(4) DEFAULT NULL,
  `control_admin` int(11) DEFAULT NULL,
  `control_historial` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `control_`
--

INSERT INTO `control_` (`año`, `control_admin`, `control_historial`) VALUES
('2019', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_admision`
--

CREATE TABLE `detalle_admision` (
  `id` int(11) NOT NULL,
  `cedula` varchar(15) NOT NULL,
  `direccion` int(200) NOT NULL,
  `correo` int(200) DEFAULT NULL,
  `celular` int(10) NOT NULL,
  `fecha_ingreso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_doctor`
--

CREATE TABLE `detalle_doctor` (
  `id` int(11) NOT NULL,
  `cedula` varchar(15) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `correo` varchar(200) DEFAULT NULL,
  `celular` varchar(10) NOT NULL,
  `a_lunes` varbinary(1) DEFAULT NULL,
  `a_martres` varbinary(1) DEFAULT NULL,
  `a_miercoles` varbinary(1) DEFAULT NULL,
  `a_jueves` varbinary(1) DEFAULT NULL,
  `a_viernes` varbinary(1) DEFAULT NULL,
  `a_sabado` varbinary(1) DEFAULT NULL,
  `a_domingos` varbinary(1) DEFAULT NULL,
  `ma_desde` varchar(5) NOT NULL,
  `ma_hasta` varchar(5) NOT NULL,
  `ta_desde` varchar(5) NOT NULL,
  `ta_hasta` varchar(5) NOT NULL,
  `fecha_ingreso` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `cedula` varchar(10) NOT NULL,
  `cod_doctor` int(11) NOT NULL,
  `nombre1` varchar(50) DEFAULT NULL,
  `nombre2` varchar(50) DEFAULT NULL,
  `apellido1` varchar(50) DEFAULT NULL,
  `apelldio2` varchar(50) DEFAULT NULL,
  `nickname` varchar(100) DEFAULT NULL,
  `pass` varchar(50) DEFAULT NULL,
  `activo` binary(1) DEFAULT NULL,
  `rol` varchar(100) DEFAULT NULL,
  `imagen` varchar(50) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `cod_especialidad` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`cedula`, `cod_doctor`, `nombre1`, `nombre2`, `apellido1`, `apelldio2`, `nickname`, `pass`, `activo`, `rol`, `imagen`, `fecha`, `cod_especialidad`) VALUES
('09000', 0, 'Christina', 'Maria', 'Yepez', 'tecnologico', 'admision', 'admision', 0x31, 'ADMISION', 'call.png', '2019-12-25', 0),
('0911', 1, 'Stevyn', 'Marcelo', 'Poveda', 'Velasquez', 'doctor1', 'doctor1', 0x31, 'DOCTOR', 'doctor.jpg', '2019-12-25', 0),
('0922', 2, 'Cristian', 'Adrian', 'Lopez', 'Aguirre', 'doctor2', 'doctor2', 0x31, 'DOCTOR', 'doctor2.jpg', '2019-12-25', 0),
('0933', 3, 'Isaac', 'Feliciano', 'Orrala', 'Tecnologico', 'doctor3', 'doctor3', 0x31, 'DOCTOR', 'doctor3.png', '2019-12-25', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admision`
--
ALTER TABLE `admision`
  ADD PRIMARY KEY (`cod_paciente`);

--
-- Indices de la tabla `agendar`
--
ALTER TABLE `agendar`
  ADD PRIMARY KEY (`cod_agenda`);

--
-- Indices de la tabla `detalle_admision`
--
ALTER TABLE `detalle_admision`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `detalle_doctor`
--
ALTER TABLE `detalle_doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`cedula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `admision`
--
ALTER TABLE `admision`
  MODIFY `cod_paciente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `agendar`
--
ALTER TABLE `agendar`
  MODIFY `cod_agenda` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_admision`
--
ALTER TABLE `detalle_admision`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_doctor`
--
ALTER TABLE `detalle_doctor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
