// Auto-generated. Do not edit!

// (in-package mservo_msg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class traj_1d {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.traj = null;
    }
    else {
      if (initObj.hasOwnProperty('traj')) {
        this.traj = initObj.traj
      }
      else {
        this.traj = new Array(7).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type traj_1d
    // Check that the constant length array field [traj] has the right length
    if (obj.traj.length !== 7) {
      throw new Error('Unable to serialize array field traj - length must be 7')
    }
    // Serialize message field [traj]
    bufferOffset = _arraySerializer.float64(obj.traj, buffer, bufferOffset, 7);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type traj_1d
    let len;
    let data = new traj_1d(null);
    // Deserialize message field [traj]
    data.traj = _arrayDeserializer.float64(buffer, bufferOffset, 7)
    return data;
  }

  static getMessageSize(object) {
    return 56;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mservo_msg/traj_1d';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '58e9b5284e3c4cd3c99f99337b97f52c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[7] traj
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new traj_1d(null);
    if (msg.traj !== undefined) {
      resolved.traj = msg.traj;
    }
    else {
      resolved.traj = new Array(7).fill(0)
    }

    return resolved;
    }
};

module.exports = traj_1d;
