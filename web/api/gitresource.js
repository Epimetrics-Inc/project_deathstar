export function getImageResource (title, filename) {
  var githuburl = 'https://raw.githubusercontent.com/hadrianpaulo/project_deathstar/master/ETL/finalized_dataset/'

  return (githuburl + title.substring(0, 4) + '/' + title + '/' + filename)
}
