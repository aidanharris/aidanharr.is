'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer');
var cssnano = require('cssnano');
var postcssDiscardComments = require('postcss-discard-comments');
var rename = require('gulp-rename');

gulp.task('sass', function () {
  return gulp.src('./sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('../static/css'));
});

gulp.task('css', ['sass'], function () {
    var processors = [
        autoprefixer({browsers: ['last 2 versions']}),
        cssnano({autoprefixer: false}),
        postcssDiscardComments({removeAll: true})
    ];
    return gulp.src('../static/css/style.css')
        .pipe(postcss(processors))
        .pipe(rename('style.min.css'))
        .pipe(gulp.dest('../static/css'));
});

gulp.task('devicons', function () {
  gulp.src([
    './devicons/fonts/*'
  ])
  .pipe(gulp.dest('../static/fonts'));
});

gulp.task('default', ['css'], function () {});
