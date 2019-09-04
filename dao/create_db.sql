
DROP TABLE IF EXISTS `emails`;
CREATE TABLE IF NOT EXISTS `emails` (
  `email` varchar(22) NOT NULL,
  `send_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `o_email` varchar(22) NOT NULL,
  `cont` text NOT NULL,
  `state` int(11) NOT NULL COMMENT '0 告白 1 感谢 2 配对成功 3 有对象'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `teenagers`
--

DROP TABLE IF EXISTS `teenagers`;
CREATE TABLE IF NOT EXISTS `teenagers` (
  `email` varchar(22) NOT NULL,
  `name` varchar(255) NOT NULL DEFAULT '',
  `sex` int(4) NOT NULL DEFAULT '-1' COMMENT '-1 保密 0 女生 1 男生',
  `o_email` varchar(22) NOT NULL,
  `o_name` varchar(255) NOT NULL DEFAULT '',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emails`
--
ALTER TABLE `emails`
  ADD PRIMARY KEY (`send_time`);

--
-- Indexes for table `teenagers`
--
ALTER TABLE `teenagers`
  ADD PRIMARY KEY (`email`);