export function secondsToRelative(seconds : number) {

    let now = Math.round((new Date().getTime() / 1000));
    let timeElapsed = now - seconds;

    if (timeElapsed < 60) {
         return  timeElapsed + ' secs ago';
    } else if (timeElapsed < 60*60) {
         return  Math.round(timeElapsed/60) + ' mins ago';
    } else if (timeElapsed < 60*60*24) {
         return  Math.round(timeElapsed/(60*60)) + ' hours ago';
    } else if (timeElapsed < 60*60*24*355) {
         return  Math.round(timeElapsed/(60*60*24)) + ' days ago';
    } else {
         return  Math.round(timeElapsed/(60*60*24*355)) + ' years ago';
    }
}