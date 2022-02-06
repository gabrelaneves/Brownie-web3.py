pragma solidity ^0.8.6;

contract SumContract {
    uint256 public value;
    uint256 public valuetoAdd;
    uint256 public valueAfterSum;
    address public owner;
    mapping(uint256 => uint256) public valuetoValueAfterSum;

    constructor() {
        owner = msg.sender;
        value = 0;
    }

    modifier OnlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function Sum(uint256 _value, uint256 _valuetoadd) public OnlyOwner {
        value += _value;
        valuetoAdd = _valuetoadd;
        valueAfterSum = value + valuetoAdd;
        valuetoValueAfterSum[value] = valueAfterSum;
    }

    function retrive() public view returns (uint256) {
        return valueAfterSum;
    }
}
