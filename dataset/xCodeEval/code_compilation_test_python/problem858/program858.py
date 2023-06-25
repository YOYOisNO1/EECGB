def program858():
    #! /usr/bin/env ruby
    
    k = gets.to_i
    m = gets.chop.split.map {|x| x.to_i}.sort.reverse
    sum = 0
    sol = m.map {|x| sum += x}.map { |i| i >= k }.find_index(true)
    
    if k.equal? 0
      p 0
    elsif sol.equal? nil
      p -1
    else
    p sol + 1
    end
    