<?php


#$dataPath = 'C:/web/data/toutiaodata/p/';
$dataPath = '..\\data\\toutiaodata\\p\\';

$file = dirname($dataPath);

#获取请求参数
$url = $_SERVER["REQUEST_URI"];
#var_dump($url);

$urlFulldate = explode('=', $url)[1];
#var_dump( $urlDate);
$urlDate = explode('/',$urlFulldate)[1];
#echo $urlDate;
#echo $dataPath,$urlDate;
$urlid = explode('/', $urlFulldate)[2];
$urlid = explode('.', $urlid)[0];
$filePath =$dataPath . $urlDate . '\\' . $urlid . '.js';

echo $filePath;

unlink($filePath);


?>