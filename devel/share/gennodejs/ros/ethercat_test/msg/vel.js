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

class vel {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.velocity = null;
    }
    else {
      if (initObj.hasOwnProperty('velocity')) {
        this.velocity = initObj.velocity
      }
      else {
        this.velocity = new Array(4).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vel
    // Check that the constant length array field [velocity] has the right length
    if (obj.velocity.length !== 4) {
      throw new Error('Unable to serialize array field velocity - length must be 4')
    }
    // Serialize message field [velocity]
    bufferOffset = _arraySerializer.int32(obj.velocity, buffer, bufferOffset, 4);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vel
    let len;
    let data = new vel(null);
    // Deserialize message field [velocity]
    data.velocity = _arrayDeserializer.int32(buffer, bufferOffset, 4)
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ethercat_test/vel';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f8dbe9fe5f891a8fdba5d30d5afaa9f6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[4] velocity
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vel(null);
    if (msg.velocity !== undefined) {
      resolved.velocity = msg.velocity;
    }
    else {
      resolved.velocity = new Array(4).fill(0)
    }

    return resolved;
    }
};

module.exports = vel;
