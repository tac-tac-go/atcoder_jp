/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	            -1 if num is lower than the guess number
 *			             1 if num is higher than the guess number
 *                       otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let row = 0
    let high = n
    let middle;
    while(row<=high){
        middle=parseInt((row+high)/2)
        if(guess(middle)==0){
            return middle
            break
        }else if(guess(middle)==-1){
            high = middle-1
        }else{
            row = middle+1
        }
    }
};
