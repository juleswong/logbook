app.factory('logbook', ['$http', function($http) {
	return $http.get('http://127.0.0.1:8000/info/api/?format=json')
		.success(function(data) {
			return data;
		})
		.error(function(err) {
			return err;
		})
}])