const { DateTime } = require("luxon");

module.exports = function (eleventyConfig) {
  // Copy the `css` directory to the output
  eleventyConfig.addPassthroughCopy('css');

  // Watch the `css` directory for changes
  eleventyConfig.addWatchTarget('css');

  eleventyConfig.addFilter("fDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj).setLocale('en-us').toLocaleString(DateTime.DATE_FULL);
  });

  eleventyConfig.addFilter("cDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj).setLocale('en-gb').toLocaleString();
  });

  return {
    dir: {
      output: "docs"
    }
  }
};