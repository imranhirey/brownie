// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

contract Simplestorage {
    uint256 public imran=90;
    function get() public view returns (uint256) {
        return imran;
    }
    function badalimran(uint256 _imrann) public returns (uint256) {
        imran = _imrann;
        return imran;
    }

    struct People {
        string magaca;
        uint256 lambarka;
    }
    People public person = People({lambarka: 67, magaca: "imran"});
    People public person2 = People({lambarka: 97, magaca: "ubeid"});

    People[] public people;

    function addperson(string memory _name, uint256 _favouratenumber) public {
        people.push(People(_name, _favouratenumber));
    }
}
