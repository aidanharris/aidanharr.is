'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

var sassTask = function () {
  return gulp.src('./sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('../static/css'));
};

var deviconsTask = function() {
  gulp.src([
    './devicons/fonts/*',
  ])
  .pipe(gulp.dest('../static/fonts'));
};

gulp.task('sass', sassTask);
gulp.task('devicons', deviconsTask);

gulp.task('default', function() {
  sassTask();
  deviconsTask();
});
