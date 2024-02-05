-- 1. Вывести названия всех стран Евразии
select name
  from country
 where continent in ('Europe', 'Asia');

-- +---------------------+
-- | name                |
-- +---------------------+
-- | Afghanistan         |
-- | Albania             |
-- | Andorra             |
-- .......................
-- | Yemen               |
-- | Yugoslavia          |
-- +---------------------+
-- 97 rows in set (0.0082 sec) 


-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
select region, name as country
  from country
 where lifeexpectancy < 50;
 
-- +---------------------------+-------------+
-- | region                    | country     |
-- +---------------------------+-------------+
-- | Southern and Central Asia | Afghanistan |
-- | Central Africa            | Angola      |
-- | Eastern Africa            | Burundi     |
-- | Western Africa            | Burkina Faso|
-- ...........................................
-- | Southeast Asia            | East Timor  |
-- | Eastern Africa            | Uganda      |
-- | Eastern Africa            | Zambia      |
-- | Eastern Africa            | Zimbabwe    |
-- +---------------------------+-------------+
-- 28 rows in set (0.0007 sec) 

 
-- 3. Вывести название самой крупной по площади страны Африки
  select name
    from country
   where continent = 'Africa'
order by surfacearea desc
   limit 1;

-- +-------+
-- | name  |
-- +-------+
-- | Sudan |
-- +-------+
-- 1 row in set (0.0006 sec)
   
   
-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
  select name,
         population / surfacearea as 'density'
    from country
   where continent = 'Asia'
order by density
   limit 5;

-- +--------------+---------+
-- | name         | density |
-- +--------------+---------+
-- | Mongolia     |  1.6993 |
-- | Kazakstan    |  5.9536 |
-- | Oman         |  8.2132 |
-- | Turkmenistan |  9.1354 |
-- | Saudi Arabia | 10.0512 |
-- +--------------+---------+
-- 5 rows in set (0.0006 sec)


-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек
  select countrycode,
         name
    from city
   where population >= 5000000
order by population;

-- +-------------+-------------------+
-- | countrycode | name              |
-- +-------------+-------------------+
-- | PAK         | Lahore            |
-- | COD         | Kinshasa          |
-- | CHN         | Tianjin           |
-- | BRA         | Rio de Janeiro    |
-- | COL         | Santafé de Bogotá |
-- | THA         | Bangkok           |
-- | CHN         | Chongqing         |
-- | PER         | Lima              |
-- | IRN         | Teheran           |
-- | EGY         | Cairo             |
-- | IND         | Delhi             |
-- | GBR         | London            |
-- | CHN         | Peking            |
-- | JPN         | Tokyo             |
-- | USA         | New York          |
-- | RUS         | Moscow            |
-- | MEX         | Ciudad de México  |
-- | TUR         | Istanbul          |
-- | PAK         | Karachi           |
-- | IDN         | Jakarta           |
-- | CHN         | Shanghai          |
-- | BRA         | São Paulo         |
-- | KOR         | Seoul             |
-- | IND         | Mumbai (Bombay)   |
-- +-------------+-------------------+
-- 24 rows in set (0.0021 sec)

-- 6. Вывести название города в Индии с самым длинным названием
--      для подсчёта количества символов используйте встроенную функцию char_length()
  select name       
    from city
   where countrycode = 'IND'
order by char_length(name) desc
   limit 1;

-- +--------------------------------+
-- | name                           |
-- +--------------------------------+
-- | Thiruvananthapuram (Trivandrum |
-- +--------------------------------+
-- 1 row in set (0.0009 sec)