    Teams = ["BERLAND"]
def teamn(name)
      Teams << name if Teams.index(name).nil?
      Teams.index(name)
    end
    game = [1,0,0,0]
    point = [3,0,0,0]
    diff = [0,0,0,0]
    earn = [0,0,0,0]
    5.times do |i|
      input = gets.split(" ")
      teama = teamn(input[0])
      teamb = teamn(input[1])
      score = input[2].split(":").map{|x| x.to_i}
      if score[0]>score[1]
        point[teama] += 3
      elsif score[0]==score[1]
        point[teama] += 1
        point[teamb] += 1
      else
        point[teamb] += 3
      end
      game[teama] += 1
      game[teamb] += 1
      diff[teama] += score[0] - score[1]
      diff[teamb] += score[1] - score[0]
      earn[teama] += score[0]
      earn[teamb] += score[1]
    end
    opponent = game.index(2)
    found = false
    fi = nil
    fj = nil
    1.upto(50) do |i|
      diff[0] += i
      diff[opponent] -= i
      i.upto(50) do |j|
        earn[0] += j
        earn[opponent] += j-i
        rank = (0..3).sort{|a,b| (point[a]<=>point[b])*8+(diff[a]<=>diff[b])*4+(earn[a]<=>earn[b])*2-(Teams[a]<=>Teams[b])}.index(0)
        if rank > 1
          found = true
          fj = j
          break
        end
        earn[0] -= j
        earn[opponent] -= j-i
      end
      if found
        fi = i
        break
      end
      diff[0] -= i
      diff[opponent] += i
    end
    if found
      puts fj.to_s+":"+(fj-fi).to_s
    else
      puts "IMPOSSIBLE"
    end