const assert = require('chai').assert;
const myApp = require('../src/main.js')

desccribe('Factorial', function() {
    describe("handle valid input", function(){
        it("should return 6 as factorial for 3", function() {
            assert.equal(myApp.computeFactorial(3), 6);
        });
    })
    describe("handle invalid input", function(){
        it("should return undefined as Factorial for -5", function() {
            assert.equal(myApp.computeFactorial(-5), 'undefined')
        });
    })
})
