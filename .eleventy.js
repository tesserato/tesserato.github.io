const { DateTime } = require("luxon");



module.exports = function (eleventyConfig) {

  // let markdownIt = require("markdown-it");
  // let markdownItTaskLists = require("markdown-it-task-lists");
  // let options = {
  //   html: true
  // };
  // let markdownLib = markdownIt(options).use(markdownItTaskLists);   
  // eleventyConfig.setLibrary("md", markdownLib);


  // Copy the `css` directory to the output
  eleventyConfig.addPassthroughCopy('css');

  // Copy the `css` directory to the output
  eleventyConfig.addPassthroughCopy('ttf');

  // Watch the `css` directory for changes
  eleventyConfig.addWatchTarget('css');

  eleventyConfig.addFilter("fDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj).setLocale('en-us').toLocaleString(DateTime.DATE_FULL);
  });

  eleventyConfig.addFilter("cDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj).setLocale('en-gb').toLocaleString();
  });

  // fetch(url).then(res => res.text())

  return {
    dir: {
      output: "docs"
    }
  }
};