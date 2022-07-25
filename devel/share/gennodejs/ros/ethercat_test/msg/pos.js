// Auto-generated. Do not edit!

// (in-package ethercat_test.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class pos {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.position = null;
    }
    else {
      if (initObj.hasOwnProperty('position')) {
        this.position = initObj.position
      }
      else {
        this.position = new Array(7).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type pos
    // Check that the constant length array field [position] has the right length
    if (obj.position.length !== 7) {
      throw new Error('Unable to serialize array field position - length must be 7')
    }
    // Serialize message field [position]
    bufferOffset = _arraySerializer.int32(obj.position, buffer, bufferOffset, 7);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type pos
    let len;
    let data = new pos(null);
    // Deserialize message field [position]
    data.position = _arrayDeserializer.int32(buffer, bufferOffset, 7)
    return data;
  }

  static getMessageSize(object) {
    return 28;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ethercat_test/pos';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'fa44e48694f6c8d9c41d364ed0879145';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[7] position
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new pos(null);
    if (msg.position !== undefined) {
      resolved.position = msg.position;
    }
    else {
      resolved.position = new Array(7).fill(0)
    }

    return resolved;
    }
};

module.exports = pos;
