// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract sms {
  // dynamic 
  string[] _msgs; // state variables 

  function insertMessage(string memory m) public {
    _msgs.push(m); // push - appends the m into _msgs
  }

  function viewMessages() public view returns(string[] memory){
    return (_msgs);
  }
}
