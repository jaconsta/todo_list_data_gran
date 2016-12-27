var $ = require('gulp-load-plugins')();
var argv = require('yargs').argv;
var gulp     = require('gulp');
var rimraf   = require('rimraf');
var sequence = require('run-sequence');
var browser = require('browser-sync');

var browserify = require('browserify');
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');
var concat = require('gulp-concat');

// Check for --production flag
var isProduction = !!(argv.production);

// Port to use for the development server.
var PORT = 8000;

// Delete the "dist" folder at start
gulp.task('clean', function(done) {
  rimraf('dist', done);
});

// Hadle html files
gulp.task('pages', function() {
  return gulp.src('./src/pages/**/*.html')
    .pipe(gulp.dest('dist'))
});

// Move css library files.
gulp.task('css', [], function() {
    gulp.src('./src/css/**.**')
        .pipe(gulp.dest('dist/css'));
});

// Move js library files.
gulp.task('javascript_libs', [], function() {
    gulp.src('./src/js/**.**')
        .pipe(gulp.dest('dist/js'));
});

// Compile coffeescript files and Browserify
gulp.task('javascript', function() {

  var b = browserify({
    entries: './src/coffeescripts/app.coffee',
    debug: true
  })

  return b.transform('coffeeify', {extensions: ['.coffee']})
  .bundle()
  .pipe(source('./app.js'))
  .pipe(buffer())
  .pipe($.sourcemaps.init({loadMaps: true}))
  .on('error', console.log)
  .pipe(gulp.dest('dist/js'));
    // return gulp.src('./src/cofeescripts/*.coffee', { read: false })
    //            .pipe(browserify({ transform: ['coffeeify'], extensions: ['.coffee'] }))
    //            //.pipe(concat('index.js'))
    //            .pipe(gulp.dest('./dist/js'));
});

// Run all compilation taks and build the "dist" folder 
gulp.task('build', function(done) {
  sequence('clean', ['pages', 'css', 'javascript_libs', 'javascript'], done);
});

// Start a server with LiveReload
gulp.task('server', ['build'], function() {
  browser.init({
    server: 'dist', port: PORT
  });
});

// Build and watch
gulp.task('default', ['build', 'server'], function() {
  gulp.watch(['src/pages/**/*.html'], ['pages', browser.reload]);
  gulp.watch(['src/css/**/*.css'], ['css', browser.reload]);
  gulp.watch(['src/cofeescripts/**/*.coffee'], ['javascript', browser.reload]);
});