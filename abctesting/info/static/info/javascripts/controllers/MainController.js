app.controller('MainController', ['$scope', 'logbook', function($scope, logbook) {
	$scope.subtitle = 'Log Book';
	$scope.sortType = 'lab_number';
	$scope.sortReverse = true;
	$scope.searchLog = '';
	logbook.success(function(data) {
		$scope.logBook = data;
	});
}]);