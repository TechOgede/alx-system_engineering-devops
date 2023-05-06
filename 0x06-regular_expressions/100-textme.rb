#!/usr/bin/env ruby
puts ARGV[0].scan(/(\[from:(?<from>\+?\d{11})\])\s(\[to:(?<to>\+?\d{11})\])\s(\[flags:(?<flags>-?\d:-?\d:-?\d:-?\d:-?\d)\])/).join(",")
