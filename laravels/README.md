### 服务器要求
	PHP版本 >=7
	PHP扩展：OpenSSL
			PDO
			mbstring
			tokenizer
	PHP配置文件(.ini)开启：
			extension=php_openssl.dll
			extension=php_pdo_mysql.dll
			extension=php_mbstring.dll
			extension=php_fileinfo.dll
			extension=php_curl.dll

### 安装composer

### 通过composer安装laravel
	切换国内镜像
		composer config -g repo.packagist composer https://packagist.phpcomposer.com
	
	composer 部署laravel项目
		在当前目录创建一个名为laravel的laravel项目
			composer create-project laravel/laravel --prefer-dist ./
		在指定目录创建一个名为laravel的laravel项目
			composer create-project laravel/laravel --prefer-dist ./xxx
