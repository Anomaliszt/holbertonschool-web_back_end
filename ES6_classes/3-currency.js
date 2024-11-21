/*
  Create a class named Currency. It should have a constructor 
  that accepts two parameters: code and name. The code should 
  be a string, and the name should be a string. 
  The class should have the following methods:
*/
export default class Currency {
	constructor(code = '', name = '') {
	  this.code = code;
	  this.name = name;
	}
  
	displayFullCurrency() {
	  return `${this.name} (${this.code})`;
	}
  
	get code() {
	  return this._code;
	}
  
	set code(value) {
	  if (typeof value !== 'string') {
		throw new TypeError('Code must be a string');
	  }
	  this._code = value;
	}
  
	get name() {
	  return this._name;
	}
  
	set name(value) {
	  if (typeof value !== 'string') {
		throw new TypeError('Name must be a string');
	  }
	  this._name = value;
	}
  }