-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 20, 2023 at 04:28 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `doctorsite`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment_appointment`
--

CREATE TABLE `appointment_appointment` (
  `id` bigint(20) NOT NULL,
  `booking_date` date NOT NULL,
  `appt_date` date NOT NULL,
  `appt_time` varchar(20) NOT NULL,
  `doctor_id` bigint(20) DEFAULT NULL,
  `patient_id` bigint(20) DEFAULT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_appointment`
--

INSERT INTO `appointment_appointment` (`id`, `booking_date`, `appt_date`, `appt_time`, `doctor_id`, `patient_id`, `status`) VALUES
(6, '2023-07-18', '2023-07-18', '09:30 am', 1, 1, 'Accepted'),
(7, '2023-07-19', '2023-07-19', '09:30:00', 1, 1, 'New');

-- --------------------------------------------------------

--
-- Table structure for table `appointment_award`
--

CREATE TABLE `appointment_award` (
  `id` bigint(20) NOT NULL,
  `awards` varchar(100) NOT NULL,
  `award_year` varchar(100) NOT NULL,
  `doctor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_award`
--

INSERT INTO `appointment_award` (`id`, `awards`, `award_year`, `doctor_id`) VALUES
(1, 'Best Doctor', '2020', 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_chat`
--

CREATE TABLE `appointment_chat` (
  `id` bigint(20) NOT NULL,
  `message` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `receiver_id` bigint(20) NOT NULL,
  `sender_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_chat`
--

INSERT INTO `appointment_chat` (`id`, `message`, `timestamp`, `receiver_id`, `sender_id`) VALUES
(1, 'hi', '2023-07-20 09:46:06.344556', 1, 3),
(2, 'hi', '2023-07-20 09:46:57.837454', 1, 3),
(5, 'hello', '2023-07-20 10:48:55.861494', 3, 1),
(6, 'how are you', '2023-07-20 10:49:41.410578', 1, 3),
(7, 'hi', '2023-07-20 11:53:55.965432', 1, 3),
(8, 'hi', '2023-07-20 11:59:05.705524', 1, 3),
(9, 'hello hassan', '2023-07-20 12:38:41.102311', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_clinic`
--

CREATE TABLE `appointment_clinic` (
  `id` bigint(20) NOT NULL,
  `clinic_name` varchar(100) NOT NULL,
  `clinic_image` varchar(100) NOT NULL,
  `clinic_address` varchar(100) NOT NULL,
  `doctor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_clinic`
--

INSERT INTO `appointment_clinic` (`id`, `clinic_name`, `clinic_image`, `clinic_address`, `doctor_id`) VALUES
(1, 'Medicare Care', 'doctor/clinics/img/feature-09.jpg', 'Sahiwal', 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_contact`
--

CREATE TABLE `appointment_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_contact`
--

INSERT INTO `appointment_contact` (`id`, `name`, `email`, `message`, `date`) VALUES
(3, 'Asif Munir', 'nina@gmail.com', '\r\n									onbsks;jbnsls vanoaenbafnonnbrjhonbk btnpnb btb pb tb kbpb 0tbpbtb ;k 		', '2023-07-20 14:06:14.952028');

-- --------------------------------------------------------

--
-- Table structure for table `appointment_degrees`
--

CREATE TABLE `appointment_degrees` (
  `id` bigint(20) NOT NULL,
  `degree` varchar(100) NOT NULL,
  `institute` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `doctor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_degrees`
--

INSERT INTO `appointment_degrees` (`id`, `degree`, `institute`, `year`, `doctor_id`) VALUES
(1, 'MBBS', 'Medical Collage', '2014', 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_doctor`
--

CREATE TABLE `appointment_doctor` (
  `id` bigint(20) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `biography` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `postal_code` varchar(100) NOT NULL,
  `date_birth` date NOT NULL,
  `price` varchar(100) NOT NULL,
  `doc_image` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `specialization_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_doctor`
--

INSERT INTO `appointment_doctor` (`id`, `gender`, `phone`, `biography`, `address`, `city`, `country`, `state`, `postal_code`, `date_birth`, `price`, `doc_image`, `status`, `user_id`, `specialization_id`) VALUES
(1, 'Male', '4497387447', 'yyggkgyghh', 'Pakistan Punjab Sahiwal', 'Sahiwal', 'Pakistan', 'Punjab', '57000', '1998-06-10', '500', 'doctor/profile/img/doctor-03.jpg', 'active', 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_doctorschedule`
--

CREATE TABLE `appointment_doctorschedule` (
  `id` bigint(20) NOT NULL,
  `day_of_week` varchar(20) NOT NULL,
  `start_time` varchar(20) NOT NULL,
  `end_time` varchar(20) NOT NULL,
  `doctor_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_doctorschedule`
--

INSERT INTO `appointment_doctorschedule` (`id`, `day_of_week`, `start_time`, `end_time`, `doctor_id`) VALUES
(3, 'Monday', '09:30', '11:00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_experience`
--

CREATE TABLE `appointment_experience` (
  `id` bigint(20) NOT NULL,
  `hospital_name` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `doctor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_experience`
--

INSERT INTO `appointment_experience` (`id`, `hospital_name`, `designation`, `start_date`, `end_date`, `doctor_id`) VALUES
(1, 'Ghulam Momorial', 'Child', '2019-11-13', '2023-07-09', 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_patient`
--

CREATE TABLE `appointment_patient` (
  `id` bigint(20) NOT NULL,
  `date_birth` date NOT NULL,
  `blood_group` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `postal_code` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `patient_image` varchar(100) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_patient`
--

INSERT INTO `appointment_patient` (`id`, `date_birth`, `blood_group`, `address`, `city`, `country`, `state`, `postal_code`, `phone`, `gender`, `patient_image`, `user_id`) VALUES
(1, '2002-05-03', 'A+', 'dmdksm', 'abc', 'Pakistan', 'punjab', '76576', '330789247', 'Male', 'patient/profile/img/patient3.jpg', 3);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_payment`
--

CREATE TABLE `appointment_payment` (
  `id` bigint(20) NOT NULL,
  `payment_date` datetime(6) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `doctor_id` bigint(20) DEFAULT NULL,
  `patient_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_payment`
--

INSERT INTO `appointment_payment` (`id`, `payment_date`, `amount`, `status`, `doctor_id`, `patient_id`) VALUES
(2, '2023-07-19 00:00:00.000000', '500', 'False', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_review`
--

CREATE TABLE `appointment_review` (
  `id` bigint(20) NOT NULL,
  `date` datetime(6) NOT NULL,
  `message` longtext NOT NULL,
  `title` varchar(250) NOT NULL,
  `rating` int(10) UNSIGNED NOT NULL,
  `doctor_id` bigint(20) DEFAULT NULL,
  `patient_id` bigint(20) DEFAULT NULL
) ;

--
-- Dumping data for table `appointment_review`
--

INSERT INTO `appointment_review` (`id`, `date`, `message`, `title`, `rating`, `doctor_id`, `patient_id`) VALUES
(1, '2023-07-19 12:31:05.557527', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 'jjskhldlslfvjfvjfn', 3, 1, 1),
(2, '2023-07-20 07:09:12.107289', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 'smvs,nsnf', 2, 1, 1),
(3, '2023-07-20 07:09:48.349766', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It h', 'egklnlfng', 2, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_services`
--

CREATE TABLE `appointment_services` (
  `id` bigint(20) NOT NULL,
  `service` varchar(100) NOT NULL,
  `doctor_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_services`
--

INSERT INTO `appointment_services` (`id`, `service`, `doctor_id`) VALUES
(1, 'Heart Care', 1);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_specialization`
--

CREATE TABLE `appointment_specialization` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `special_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_specialization`
--

INSERT INTO `appointment_specialization` (`id`, `name`, `special_image`) VALUES
(2, 'Cardiologist', 'doctor/spatialization/image/specialities-01_p2Nobg4.png'),
(3, 'Clinical Cardiologists', 'doctor/spatialization/image/specialities-02_XbwANnC.png'),
(5, ' Electrophysiologists', 'doctor/spatialization/image/specialities-03_cxe8bxK.png'),
(6, 'Preventive Cardiologists', 'doctor/spatialization/image/specialities-04.png'),
(7, 'Cardiac Surgeons', 'doctor/spatialization/image/specialities-05.png');

-- --------------------------------------------------------

--
-- Table structure for table `appointment_subadmin`
--

CREATE TABLE `appointment_subadmin` (
  `id` bigint(20) NOT NULL,
  `date_birth` date NOT NULL,
  `blood_group` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `postal_code` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `admin_image` varchar(100) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_subadmin`
--

INSERT INTO `appointment_subadmin` (`id`, `date_birth`, `blood_group`, `address`, `city`, `country`, `state`, `postal_code`, `phone`, `gender`, `admin_image`, `user_id`) VALUES
(1, '2023-07-15', '', 'Pakpattan Punjab Sahiwal Pakistan', 'Pakpattan', 'Pakistan', 'Punjab', '57000', '03472059325', '', 'admin/profile/img/avatar-02.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_user`
--

CREATE TABLE `appointment_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_doctor` tinyint(1) NOT NULL,
  `is_patient` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment_user`
--

INSERT INTO `appointment_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_doctor`, `is_patient`, `is_admin`) VALUES
(1, 'pbkdf2_sha256$600000$PMcK1FO6McSHmGafydS69y$Rku/9MR68F1V8wPyzE9mav6p+DjWKOUpeArIrEBftPI=', '2023-07-20 12:37:06.595844', 0, 'akhtar@gmail.com', 'Akhtar', 'Fareed', 'akhtar@gmail.com', 0, 1, '2023-07-09 15:03:16.004440', 1, 0, 0),
(2, 'pbkdf2_sha256$600000$y0XlhYYQtpKhSerDBBiOIb$B90/zOkpcl8TKmEzhJa1gkUZJsL6R3zZ8HMZk7rE+Ig=', '2023-07-20 06:47:42.598446', 1, 'malik@gmail.com', 'Malik', 'Bilal', 'malik@gmail.com', 1, 1, '2023-07-09 15:09:30.496470', 0, 0, 1),
(3, 'pbkdf2_sha256$600000$sXfr1fo97PZj0R8jW6Sfrw$KSz+smqRlDJ44LK6XJKHBQQ6JHx1Oi6D4tcvDd6YKdM=', '2023-07-20 13:00:58.200473', 0, 'hassan@gmail.com', 'Hassan', 'Khan', 'hassan@gmail.com', 0, 1, '2023-07-09 15:10:30.453235', 0, 1, 0),
(4, 'pbkdf2_sha256$600000$i1jUwhpdJUg4CyJ4bMnxKC$UDqN23lQ2oxbcD6vDSMz7cHx9oYo5OQ1J37IxT507wM=', '2023-07-14 19:02:02.611303', 1, 'malik', '', '', '', 1, 1, '2023-07-14 19:01:33.981571', 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `appointment_user_groups`
--

CREATE TABLE `appointment_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `appointment_user_user_permissions`
--

CREATE TABLE `appointment_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add appointment', 6, 'add_appointment'),
(22, 'Can change appointment', 6, 'change_appointment'),
(23, 'Can delete appointment', 6, 'delete_appointment'),
(24, 'Can view appointment', 6, 'view_appointment'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add subadmin', 8, 'add_subadmin'),
(30, 'Can change subadmin', 8, 'change_subadmin'),
(31, 'Can delete subadmin', 8, 'delete_subadmin'),
(32, 'Can view subadmin', 8, 'view_subadmin'),
(33, 'Can add specialization', 9, 'add_specialization'),
(34, 'Can change specialization', 9, 'change_specialization'),
(35, 'Can delete specialization', 9, 'delete_specialization'),
(36, 'Can view specialization', 9, 'view_specialization'),
(37, 'Can add services', 10, 'add_services'),
(38, 'Can change services', 10, 'change_services'),
(39, 'Can delete services', 10, 'delete_services'),
(40, 'Can view services', 10, 'view_services'),
(41, 'Can add patient', 11, 'add_patient'),
(42, 'Can change patient', 11, 'change_patient'),
(43, 'Can delete patient', 11, 'delete_patient'),
(44, 'Can view patient', 11, 'view_patient'),
(45, 'Can add experience', 12, 'add_experience'),
(46, 'Can change experience', 12, 'change_experience'),
(47, 'Can delete experience', 12, 'delete_experience'),
(48, 'Can view experience', 12, 'view_experience'),
(49, 'Can add doctor schedule', 13, 'add_doctorschedule'),
(50, 'Can change doctor schedule', 13, 'change_doctorschedule'),
(51, 'Can delete doctor schedule', 13, 'delete_doctorschedule'),
(52, 'Can view doctor schedule', 13, 'view_doctorschedule'),
(53, 'Can add doctor', 14, 'add_doctor'),
(54, 'Can change doctor', 14, 'change_doctor'),
(55, 'Can delete doctor', 14, 'delete_doctor'),
(56, 'Can view doctor', 14, 'view_doctor'),
(57, 'Can add degrees', 15, 'add_degrees'),
(58, 'Can change degrees', 15, 'change_degrees'),
(59, 'Can delete degrees', 15, 'delete_degrees'),
(60, 'Can view degrees', 15, 'view_degrees'),
(61, 'Can add clinic', 16, 'add_clinic'),
(62, 'Can change clinic', 16, 'change_clinic'),
(63, 'Can delete clinic', 16, 'delete_clinic'),
(64, 'Can view clinic', 16, 'view_clinic'),
(65, 'Can add award', 17, 'add_award'),
(66, 'Can change award', 17, 'change_award'),
(67, 'Can delete award', 17, 'delete_award'),
(68, 'Can view award', 17, 'view_award'),
(69, 'Can add appointment status', 18, 'add_appointmentstatus'),
(70, 'Can change appointment status', 18, 'change_appointmentstatus'),
(71, 'Can delete appointment status', 18, 'delete_appointmentstatus'),
(72, 'Can view appointment status', 18, 'view_appointmentstatus'),
(73, 'Can add payment', 19, 'add_payment'),
(74, 'Can change payment', 19, 'change_payment'),
(75, 'Can delete payment', 19, 'delete_payment'),
(76, 'Can view payment', 19, 'view_payment'),
(77, 'Can add review', 20, 'add_review'),
(78, 'Can change review', 20, 'change_review'),
(79, 'Can delete review', 20, 'delete_review'),
(80, 'Can view review', 20, 'view_review'),
(81, 'Can add chat', 21, 'add_chat'),
(82, 'Can change chat', 21, 'change_chat'),
(83, 'Can delete chat', 21, 'delete_chat'),
(84, 'Can view chat', 21, 'view_chat'),
(85, 'Can add contact', 22, 'add_contact'),
(86, 'Can change contact', 22, 'change_contact'),
(87, 'Can delete contact', 22, 'delete_contact'),
(88, 'Can view contact', 22, 'view_contact');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-07-14 19:02:47.811609', '2', 'Specialization object (2)', 1, '[{\"added\": {}}]', 9, 4),
(2, '2023-07-16 04:03:19.685234', '1', 'Doctor object (1)', 2, '[{\"changed\": {\"fields\": [\"Special id\"]}}]', 14, 4),
(3, '2023-07-16 04:31:31.303066', '1', 'Doctor object (1)', 2, '[{\"changed\": {\"fields\": [\"Special\"]}}]', 14, 4),
(4, '2023-07-16 05:37:03.341999', '1', 'Doctor object (1)', 2, '[{\"changed\": {\"fields\": [\"Special\"]}}]', 14, 4),
(5, '2023-07-16 05:38:35.250706', '2', 'Services object (2)', 3, '', 10, 4),
(6, '2023-07-16 05:39:26.727320', '2', 'Clinic object (2)', 3, '', 16, 4),
(7, '2023-07-16 05:39:32.518694', '3', 'Clinic object (3)', 3, '', 16, 4);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(6, 'Appointment', 'appointment'),
(18, 'Appointment', 'appointmentstatus'),
(17, 'Appointment', 'award'),
(21, 'Appointment', 'chat'),
(16, 'Appointment', 'clinic'),
(22, 'Appointment', 'contact'),
(15, 'Appointment', 'degrees'),
(14, 'Appointment', 'doctor'),
(13, 'Appointment', 'doctorschedule'),
(12, 'Appointment', 'experience'),
(11, 'Appointment', 'patient'),
(19, 'Appointment', 'payment'),
(20, 'Appointment', 'review'),
(10, 'Appointment', 'services'),
(9, 'Appointment', 'specialization'),
(8, 'Appointment', 'subadmin'),
(7, 'Appointment', 'user'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-09 15:00:51.452416'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-07-09 15:00:51.546946'),
(3, 'auth', '0001_initial', '2023-07-09 15:00:51.854353'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-07-09 15:00:51.958998'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-07-09 15:00:51.970992'),
(6, 'auth', '0004_alter_user_username_opts', '2023-07-09 15:00:51.983980'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-07-09 15:00:51.993115'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-07-09 15:00:51.998111'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-07-09 15:00:52.009099'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-07-09 15:00:52.020667'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-07-09 15:00:52.030661'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-07-09 15:00:52.056637'),
(13, 'auth', '0011_update_proxy_permissions', '2023-07-09 15:00:52.069625'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-07-09 15:00:52.078612'),
(15, 'Appointment', '0001_initial', '2023-07-09 15:00:53.636953'),
(16, 'admin', '0001_initial', '2023-07-09 15:00:53.799751'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-07-09 15:00:53.835718'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-09 15:00:53.866711'),
(19, 'sessions', '0001_initial', '2023-07-09 15:00:53.926655'),
(20, 'Appointment', '0002_rename_specialization_specialization_name_and_more', '2023-07-14 18:13:48.435152'),
(21, 'Appointment', '0003_payment_appointment_status_alter_doctor_status_and_more', '2023-07-15 14:55:49.550021'),
(22, 'Appointment', '0004_remove_doctor_speci_id_doctor_specialization_and_more', '2023-07-16 03:04:19.037249'),
(23, 'Appointment', '0005_rename_specialization_doctor_special_id', '2023-07-16 03:33:16.745552'),
(24, 'Appointment', '0006_rename_special_id_doctor_special', '2023-07-16 04:05:12.021403'),
(25, 'Appointment', '0007_alter_doctor_special', '2023-07-16 05:34:52.968457'),
(26, 'Appointment', '0008_alter_doctor_special', '2023-07-16 07:23:00.664150'),
(27, 'Appointment', '0009_rename_special_doctor_specialization', '2023-07-16 07:33:19.390437'),
(28, 'Appointment', '0010_alter_doctor_status', '2023-07-16 08:50:20.404095'),
(29, 'Appointment', '0011_alter_doctorschedule_doctor', '2023-07-18 02:52:24.134989'),
(30, 'Appointment', '0012_alter_appointment_doctor_alter_appointment_patient', '2023-07-18 04:06:17.667646'),
(31, 'Appointment', '0013_alter_appointment_appt_time', '2023-07-18 04:12:03.842960'),
(32, 'Appointment', '0014_alter_appointment_status', '2023-07-18 08:06:24.945931'),
(33, 'Appointment', '0015_alter_appointment_status', '2023-07-19 04:13:49.096350'),
(34, 'Appointment', '0016_alter_payment_doctor_alter_payment_patient', '2023-07-19 05:26:05.442420'),
(35, 'Appointment', '0017_alter_payment_status', '2023-07-19 12:10:19.988731'),
(36, 'Appointment', '0018_review', '2023-07-19 18:08:19.266425'),
(37, 'Appointment', '0019_alter_review_message_alter_review_title', '2023-07-19 18:52:10.407419'),
(38, 'Appointment', '0020_alter_review_rating', '2023-07-19 19:47:51.988252'),
(39, 'Appointment', '0021_chat', '2023-07-20 08:51:44.842624'),
(40, 'Appointment', '0022_alter_review_message', '2023-07-20 12:57:50.074002'),
(41, 'Appointment', '0023_contact', '2023-07-20 13:24:23.794045'),
(42, 'Appointment', '0024_contact_date', '2023-07-20 14:03:26.615306');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('exheci3uo4h6ryfxal00taahozrgbvhh', '.eJxVjEEOwiAQRe_C2hCE0kGX7j0DGZgZqRpISrsy3l2bdKHb_977LxVxXUpcO89xInVWTh1-t4T5wXUDdMd6azq3usxT0puid9r1tRE_L7v7d1Cwl29tvZA5EWYY3dEMwQmDCOSUwCAxEFsWD856pCF4D2GwAHZEFJBRnHp_APmGOEs:1qMTH8:aMDdW8pkObSW0t7jlTAmDBEUGKE_DyOPWp4-Wm0a2-g', '2023-08-03 13:00:58.209610'),
('gmzd21c50gvqp3gvqjurw9v1tt2etqs9', '.eJxVjEEOwiAQRe_C2hCE0kGX7j0DGZgZqRpISrsy3l2bdKHb_977LxVxXUpcO89xInVWTh1-t4T5wXUDdMd6azq3usxT0puid9r1tRE_L7v7d1Cwl29tvZA5EWYY3dEMwQmDCOSUwCAxEFsWD856pCF4D2GwAHZEFJBRnHp_APmGOEs:1qMSun:UrI3V1Mt088Rj5EIoNWnZyFX7GxID4Tac61kslybGmc', '2023-08-03 12:37:53.741953'),
('wh7adlgiy2rtfv4u4mvdnby9irync1dz', '.eJxVjDsOwjAQBe_iGllaf2IvJT1nsLzZNQ4gR4qTCnF3iJQC2jcz76VS3taati5LmlidlVGn343y-JC2A77ndpv1OLd1mUjvij5o19eZ5Xk53L-Dmnv91o4BMTubfSQuZcBIlgMEBAfiYyE0nt1gnQDFiBhKMQGkCAADEaj3B9qhN8E:1qMNRu:_WD1Wn-9Mmdf9qq4nbn3xzs2v37IMS_G59w6DnzhvI4', '2023-08-03 06:47:42.601221');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment_appointment`
--
ALTER TABLE `appointment_appointment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_appointm_doctor_id_5b220a42_fk_Appointme` (`doctor_id`),
  ADD KEY `Appointment_appointm_patient_id_ee62c42a_fk_Appointme` (`patient_id`);

--
-- Indexes for table `appointment_award`
--
ALTER TABLE `appointment_award`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_award_doctor_id_f4bde59a_fk_Appointment_user_id` (`doctor_id`);

--
-- Indexes for table `appointment_chat`
--
ALTER TABLE `appointment_chat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_chat_receiver_id_4f61b4b3_fk_Appointment_user_id` (`receiver_id`),
  ADD KEY `Appointment_chat_sender_id_bb7e5aec_fk_Appointment_user_id` (`sender_id`);

--
-- Indexes for table `appointment_clinic`
--
ALTER TABLE `appointment_clinic`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_clinic_doctor_id_c51d4d5e_fk_Appointment_user_id` (`doctor_id`);

--
-- Indexes for table `appointment_contact`
--
ALTER TABLE `appointment_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appointment_degrees`
--
ALTER TABLE `appointment_degrees`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_degrees_doctor_id_7ee9453f_fk_Appointment_user_id` (`doctor_id`);

--
-- Indexes for table `appointment_doctor`
--
ALTER TABLE `appointment_doctor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `Appointment_doctor_special_id_1f5cb532` (`specialization_id`);

--
-- Indexes for table `appointment_doctorschedule`
--
ALTER TABLE `appointment_doctorschedule`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_doctorsc_doctor_id_fb540f4d_fk_Appointme` (`doctor_id`);

--
-- Indexes for table `appointment_experience`
--
ALTER TABLE `appointment_experience`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_experience_doctor_id_952d7684_fk_Appointment_user_id` (`doctor_id`);

--
-- Indexes for table `appointment_patient`
--
ALTER TABLE `appointment_patient`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `appointment_payment`
--
ALTER TABLE `appointment_payment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_payment_doctor_id_1468eb3a_fk_Appointment_doctor_id` (`doctor_id`),
  ADD KEY `Appointment_payment_patient_id_e1dc44e7_fk_Appointme` (`patient_id`);

--
-- Indexes for table `appointment_review`
--
ALTER TABLE `appointment_review`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_review_doctor_id_3ff30312_fk_Appointment_doctor_id` (`doctor_id`),
  ADD KEY `Appointment_review_patient_id_c1463106_fk_Appointment_patient_id` (`patient_id`);

--
-- Indexes for table `appointment_services`
--
ALTER TABLE `appointment_services`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Appointment_services_doctor_id_b3eca714_fk_Appointment_user_id` (`doctor_id`);

--
-- Indexes for table `appointment_specialization`
--
ALTER TABLE `appointment_specialization`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `appointment_subadmin`
--
ALTER TABLE `appointment_subadmin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `appointment_user`
--
ALTER TABLE `appointment_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `appointment_user_groups`
--
ALTER TABLE `appointment_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Appointment_user_groups_user_id_group_id_e6ded878_uniq` (`user_id`,`group_id`),
  ADD KEY `Appointment_user_groups_group_id_3a0417b2_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `appointment_user_user_permissions`
--
ALTER TABLE `appointment_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Appointment_user_user_pe_user_id_permission_id_16ac5c03_uniq` (`user_id`,`permission_id`),
  ADD KEY `Appointment_user_use_permission_id_115a2bf1_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_Appointment_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment_appointment`
--
ALTER TABLE `appointment_appointment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `appointment_award`
--
ALTER TABLE `appointment_award`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `appointment_chat`
--
ALTER TABLE `appointment_chat`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `appointment_clinic`
--
ALTER TABLE `appointment_clinic`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `appointment_contact`
--
ALTER TABLE `appointment_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `appointment_degrees`
--
ALTER TABLE `appointment_degrees`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `appointment_doctor`
--
ALTER TABLE `appointment_doctor`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `appointment_doctorschedule`
--
ALTER TABLE `appointment_doctorschedule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `appointment_experience`
--
ALTER TABLE `appointment_experience`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `appointment_patient`
--
ALTER TABLE `appointment_patient`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `appointment_payment`
--
ALTER TABLE `appointment_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `appointment_review`
--
ALTER TABLE `appointment_review`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appointment_services`
--
ALTER TABLE `appointment_services`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `appointment_specialization`
--
ALTER TABLE `appointment_specialization`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `appointment_subadmin`
--
ALTER TABLE `appointment_subadmin`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `appointment_user`
--
ALTER TABLE `appointment_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `appointment_user_groups`
--
ALTER TABLE `appointment_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appointment_user_user_permissions`
--
ALTER TABLE `appointment_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment_appointment`
--
ALTER TABLE `appointment_appointment`
  ADD CONSTRAINT `Appointment_appointm_doctor_id_5b220a42_fk_Appointme` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_doctor` (`id`),
  ADD CONSTRAINT `Appointment_appointm_patient_id_ee62c42a_fk_Appointme` FOREIGN KEY (`patient_id`) REFERENCES `appointment_patient` (`id`);

--
-- Constraints for table `appointment_award`
--
ALTER TABLE `appointment_award`
  ADD CONSTRAINT `Appointment_award_doctor_id_f4bde59a_fk_Appointment_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_chat`
--
ALTER TABLE `appointment_chat`
  ADD CONSTRAINT `Appointment_chat_receiver_id_4f61b4b3_fk_Appointment_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `appointment_user` (`id`),
  ADD CONSTRAINT `Appointment_chat_sender_id_bb7e5aec_fk_Appointment_user_id` FOREIGN KEY (`sender_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_clinic`
--
ALTER TABLE `appointment_clinic`
  ADD CONSTRAINT `Appointment_clinic_doctor_id_c51d4d5e_fk_Appointment_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_degrees`
--
ALTER TABLE `appointment_degrees`
  ADD CONSTRAINT `Appointment_degrees_doctor_id_7ee9453f_fk_Appointment_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_doctor`
--
ALTER TABLE `appointment_doctor`
  ADD CONSTRAINT `Appointment_doctor_specialization_id_cc69f094_fk_Appointme` FOREIGN KEY (`specialization_id`) REFERENCES `appointment_specialization` (`id`),
  ADD CONSTRAINT `Appointment_doctor_user_id_33cf9d3a_fk_Appointment_user_id` FOREIGN KEY (`user_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_doctorschedule`
--
ALTER TABLE `appointment_doctorschedule`
  ADD CONSTRAINT `Appointment_doctorsc_doctor_id_fb540f4d_fk_Appointme` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_doctor` (`id`);

--
-- Constraints for table `appointment_experience`
--
ALTER TABLE `appointment_experience`
  ADD CONSTRAINT `Appointment_experience_doctor_id_952d7684_fk_Appointment_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_patient`
--
ALTER TABLE `appointment_patient`
  ADD CONSTRAINT `Appointment_patient_user_id_5ff5d1d4_fk_Appointment_user_id` FOREIGN KEY (`user_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_payment`
--
ALTER TABLE `appointment_payment`
  ADD CONSTRAINT `Appointment_payment_doctor_id_1468eb3a_fk_Appointment_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_doctor` (`id`),
  ADD CONSTRAINT `Appointment_payment_patient_id_e1dc44e7_fk_Appointme` FOREIGN KEY (`patient_id`) REFERENCES `appointment_patient` (`id`);

--
-- Constraints for table `appointment_review`
--
ALTER TABLE `appointment_review`
  ADD CONSTRAINT `Appointment_review_doctor_id_3ff30312_fk_Appointment_doctor_id` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_doctor` (`id`),
  ADD CONSTRAINT `Appointment_review_patient_id_c1463106_fk_Appointment_patient_id` FOREIGN KEY (`patient_id`) REFERENCES `appointment_patient` (`id`);

--
-- Constraints for table `appointment_services`
--
ALTER TABLE `appointment_services`
  ADD CONSTRAINT `Appointment_services_doctor_id_b3eca714_fk_Appointment_user_id` FOREIGN KEY (`doctor_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_subadmin`
--
ALTER TABLE `appointment_subadmin`
  ADD CONSTRAINT `Appointment_subadmin_user_id_bfe3b126_fk_Appointment_user_id` FOREIGN KEY (`user_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_user_groups`
--
ALTER TABLE `appointment_user_groups`
  ADD CONSTRAINT `Appointment_user_groups_group_id_3a0417b2_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `Appointment_user_groups_user_id_2a46a84c_fk_Appointment_user_id` FOREIGN KEY (`user_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `appointment_user_user_permissions`
--
ALTER TABLE `appointment_user_user_permissions`
  ADD CONSTRAINT `Appointment_user_use_permission_id_115a2bf1_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `Appointment_user_use_user_id_124d308b_fk_Appointme` FOREIGN KEY (`user_id`) REFERENCES `appointment_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Appointment_user_id` FOREIGN KEY (`user_id`) REFERENCES `appointment_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
