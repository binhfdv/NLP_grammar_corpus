import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[num=?a,pos=infront,sub=?x] VP[num=?a,pos=behind,sub=?x]
NP[num=?a,pos=?z,sub=?x]           -> NP1[num=?a,pos=?z,sub=?x] PP[]
NP[num=?a,pos=?z,sub=?x]           -> NP1[cc=?b,num=?a,pos=?z,sub=?x]    CC[cc=?b]    NP[cc=?b,num=?a,pos=?z,sub=?x]
NP[num=?a,pos=?z,sub=?x]           -> CC[cc=?b] NP[cc=?b,pos=?z,sub=?x]    CC[cc=?b]    NP[cc=?b,num=?a,pos=?z,sub=?x]
NP[num=?a,pos=?z,sub=?x]           -> DT[cc=?b] NP[cc=?b,pos=?z,sub=?x]    CC[cc=?b]    NP[cc=?b,num=?a,pos=?z,sub=?x]
NP[num=?a,pos=?z,sub=?x]           -> NPP[num=?a,pos=?z,sub=?x] 
NP[num=?a]                         -> NNP[num=?a]
NP[num=?a]                         -> NNS[num=?a]
NP[num=?a]                         -> NN[num=?a]
NP[num=?a,pos=?z,sub=?x]           -> ADJP[jj=?d]  NP[jj=?d,num=?a,pos=?z,sub=?x]
NP[num=?a,pos=?z,sub=?x]           -> DT[det=?e]   NP[det=?e,num=?a,pos=?z,sub=?x]
        
NP1[num=?a,pos=?z,sub=?x]           -> CC[cc=?b] NP[cc=?b,pos=?z,sub=?x]    CC[cc=?b]    NP[cc=?b,num=?a,pos=?z,sub=?x]
NP1[num=?a,pos=?z,sub=?x]           -> DT[cc=?b] NP[cc=?b,pos=?z,sub=?x]    CC[cc=?b]    NP[cc=?b,num=?a,pos=?z,sub=?x]
NP1[num=?a,pos=?z,sub=?x]           -> NPP[num=?a,pos=?z,sub=?x] 
NP1[num=?a]                         -> NNP[num=?a]
NP1[num=?a]                         -> NNS[num=?a]
NP1[num=?a]                         -> NN[num=?a]
NP1[num=?a,pos=?z,sub=?x]           -> ADJP[jj=?d]  NP[jj=?d,num=?a,pos=?z,sub=?x]
NP1[num=?a,pos=?z,sub=?x]           -> DT[det=?e]   NP[det=?e,num=?a,pos=?z,sub=?x]


ADJP[jj=?d]   ->  JJ[jj=?d]

VP[sub=?x,num=?a]    ->  VP1[sub=?x,num=?a]   VP[sub=?x]
VP[sub=?x,num=?a]    ->  VP1[sub=?x,num=?a]   PP[]
VP[sub=?x,num=?a]    ->  VP1[sub=?x,num=?a]   RB[]
VP[sub=?x,num=?a]    ->  VBP[sub=?x,num=?a]
VP[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   PP[]
VP[sub=?x,num=?a]    ->  VBP[sub=?x,num=?a]   PP[]
VP[sub=?x,num=?a]    ->  VBP[sub=?x,num=?a]   ADJP[]
VP[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   ADJP[]
VP[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   VBD[]
VP[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   VB[]
VP[sub=?x,num=?a]    ->  VB[rb=?y,num=?a]    RB[rb=?y]
VP[sub=?x,num=?a]    ->  VB[sub=?x,num=?a]
VP[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]
VP[sub=?x,num=?a]    ->  TO[]    VP[to=to]
VP[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   VP[]
VP[sub=?x,num=?a]    ->  VB[sub=?x,num=?a]    ADJP[] 
VP[sub=?x,pos=?z,num=?a]    ->  VBD[sub=?x,num=?a]   NP[pos=?z]
VP[sub=?x,pos=?z,num=?a]    ->  VBP[sub=?x,num=?a]   NP[pos=?z]
VP[sub=?x,pos=?z,num=?a]    ->  VBZ[sub=?x,num=?a]   NP[pos=?z]
VP[sub=?x,pos=?z,num=?a]    ->  VBZ[sub=?x,num=?a]   NP[pos=?z]    VP[]
VP[sub=?x,pos=?z,num=?a]    ->  VB[sub=?x,num=?a]    NP[pos=?z]


VP1[sub=?x,num=?a]    ->  VBP[sub=?x,num=?a]
VP1[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   PP[]
VP1[sub=?x,num=?a]    ->  VBP[sub=?x,num=?a]   PP[]
VP1[sub=?x,num=?a]    ->  VBP[sub=?x,num=?a]   ADJP[]
VP1[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   ADJP[]
VP1[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   VBD[]
VP1[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   VB[]
VP1[sub=?x,num=?a]    ->  VB[rb=?y,num=?a]    RB[rb=?y]
VP1[sub=?x,num=?a]    ->  VB[sub=?x,num=?a]
VP1[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]
VP1[sub=?x,num=?a]    ->  TO[]    VP[to=to]
VP1[sub=?x,num=?a]    ->  VBZ[sub=?x,num=?a]   VP[]
VP1[sub=?x,num=?a]    ->  VB[sub=?x,num=?a]    ADJP[] 
VP1[sub=?x,pos=?z,num=?a]    ->  VBD[sub=?x,num=?a]   NP[pos=?z]
VP1[sub=?x,pos=?z,num=?a]    ->  VBP[sub=?x,num=?a]   NP[pos=?z]
VP1[sub=?x,pos=?z,num=?a]    ->  VBZ[sub=?x,num=?a]   NP[pos=?z]
VP1[sub=?x,pos=?z,num=?a]    ->  VBZ[sub=?x,num=?a]   NP[pos=?z]    VP[]
VP1[sub=?x,pos=?z,num=?a]    ->  VB[sub=?x,num=?a]    NP[pos=?z]

PP[]    -> IN[in=?c] NP[in=?c]
  



TO[to=to]   ->  'to'

JJ[jj=abroad]   ->  'abroad'
JJ[jj=cheap]    ->  'cheap'
JJ[jj=red]      ->  'red'
JJ[jj=hot]      ->  'hot'
JJ[jj=right]    ->  'right'
JJ[jj=popular]  ->  'popular'
JJ[jj=many]     ->  'many'
JJ[jj=all]      ->  'all'
JJ[jj=nice]     ->  'nice'
JJ[jj=tall]     ->  'tall'
JJ[jj=brown]    ->  'brown'
JJ[jj=blonde]   ->  'blonde'
JJ[jj=good]     ->  'good'
JJ[jj=chinese]  ->  'chinese'
JJ[jj=young]    ->  'young'
JJ[jj=little]   ->  'little'

RB[rb=soon]     -> 'soon'
RB[rb=well]     -> 'well'


VB[sub=i,to=to,rb=soon]            -> 'sleep'|'speak'|'rent'|'become'

VBP[sub=human, rb=soon,num=pl]     -> 'help'|'fly'|'run'
VBP[sub=human, rb=well, num=pl]    -> 'warm_up'|'sleep'|'speak'|'live'
VBP[sub=animal, rb=soon,num=pl]    -> 'fly'|'run'
VBP[sub=human, num=pl]             -> 'steal'|'rent'|'have'|'swim'|'help'|'dislike'|'run'

                                   
VBZ[sub=human,rb=well,num=sg]      -> 'plays'
VBZ[sub=human,rb=soon,num=sg]      -> 'walks'
VBZ[sub=human,rb=soon,num=sg]      -> 'has'|'wears'|'likes'|'dreams'|'advises'|'agrees'|'reads'
VBZ[sub=human,num=sg]              -> 'is'
VBZ[sub=human,num=pl]              -> 'are'

VBD[sub=human,rb=soon,num=pl]      -> 'bought'|'permitted'|'restricted'
VBD[sub=human,rb=soon,num=sg]      -> 'bought'|'permitted'|'restricted'


DT[det=the]         -> 'the'
DT[det=a]           -> 'a'
DT[det=an]          -> 'an'
DT[cc=either_or]    -> 'either'

CC[cc=and]          -> 'and'
CC[cc=or]           -> 'or'
CC[cc=both_and]     -> 'both'|'and'
CC[cc=neither_nor]  -> 'neither'|'nor'
CC[cc=either_or]    -> 'or'

IN[in=in]       -> 'in'
IN[in=of]       -> 'of'
IN[in=with]     -> 'with'
IN[in=before]   -> 'before'
IN[in=by]       -> 'by'

NPP[cc=neither_nor,sub=human,num=pl,jj=hot,pos=infront]         -> 'i'
NPP[cc=neither_nor,sub=human,num=pl,jj=nice,pos=infront]        -> 'i'
NPP[cc=neither_nor,sub=human,num=pl,jj=tall,pos=infront]        -> 'i'
NPP[cc=neither_nor,sub=human,num=pl,jj=good,pos=infront]        -> 'i'
NPP[cc=neither_nor,sub=human,num=pl,jj=chinese,pos=infront]     -> 'i'
NPP[cc=neither_nor,sub=human,num=pl,jj=young,pos=infront]       -> 'i'

NPP[cc=and,sub=human,num=pl,jj=hot,pos=infront]                 -> 'i'
NPP[cc=and,sub=human,num=pl,jj=nice,pos=infront]                -> 'i'
NPP[cc=and,sub=human,num=pl,jj=tall,pos=infront]                -> 'i'
NPP[cc=and,sub=human,num=pl,jj=good,pos=infront]                -> 'i'
NPP[cc=and,sub=human,num=pl,jj=chinese,pos=infront]             -> 'i'
NPP[cc=and,sub=human,num=pl,jj=young,pos=infront]               -> 'i'

NPP[cc=and,pos=behind] -> 'me'

NPP[sub=human,num=sg,jj=hot,pos=infront]                    -> 'she'|'he'
NPP[sub=human,num=sg,jj=nice,pos=infront]                   -> 'she'|'he'
NPP[sub=human,num=sg,jj=tall,pos=infront]                   -> 'she'|'he'
NPP[sub=human,num=sg,jj=good,pos=infront]                   -> 'she'|'he'
NPP[sub=human,num=sg,jj=chinese,pos=infront]                -> 'she'|'he'
NPP[sub=human,num=sg,jj=young,pos=infront]                  -> 'she'|'he'

NPP[sub=sth,num=sg,jj=hot,in=with,pos=?z]              -> 'it'
NPP[sub=sth,num=sg,jj=nice,in=with,pos=?z]             -> 'it'
NPP[sub=sth,num=sg,jj=good,in=with,pos=?z]             -> 'it'
NPP[sub=sth,num=sg,jj=brown,in=with,pos=?z]            -> 'it'

NNS[cc=neither_nor,sub=human,num=pl,jj=hot,in=with,pos=?z]        ->'you'
NNS[cc=neither_nor,sub=human,num=pl,jj=nice,in=with,pos=?z]       ->'you'
NNS[cc=neither_nor,sub=human,num=pl,jj=tall,in=with,pos=?z]       ->'you'
NNS[cc=neither_nor,sub=human,num=pl,jj=good,in=with,pos=?z]       ->'you'
NNS[cc=neither_nor,sub=human,num=pl,jj=chinese,in=with,pos=?z]    ->'you'
NNS[cc=neither_nor,sub=human,num=pl,jj=young,in=with,pos=?z]      ->'you'
      
NNS[cc=and,sub=human,num=pl,jj=hot,in=with,pos=?z]                -> 'you'
NNS[cc=and,sub=human,num=pl,jj=nice,in=with,pos=?z]               -> 'you'
NNS[cc=and,sub=human,num=pl,jj=tall,in=with,pos=?z]               -> 'you'
NNS[cc=and,sub=human,num=pl,jj=good,in=with,pos=?z]               -> 'you'
NNS[cc=and,sub=human,num=pl,jj=chinese,in=with,pos=?z]            -> 'you'
NNS[cc=and,sub=human,num=pl,jj=young,in=with,pos=?z]              -> 'you'

NNS[det=the,sub=animals,num=pl,jj=red,in=with]             ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=little,in=with]          ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=many,in=with]            ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=all,in=with]             ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=nice,in=with]            ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=brown,in=with]           ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=good,in=with]            ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=chinese,in=with]         ->'cats'|'dogs'|'birds'|'animals'|'buffallos'

NNS[det=the,sub=animals,num=pl,jj=red,in=of]               ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=little,in=of]            ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=many,in=of]              ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=all,in=of]               ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=nice,in=of]              ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=brown,in=of]             ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=good,in=of]              ->'cats'|'dogs'|'birds'|'animals'|'buffallos'
NNS[det=the,sub=animals,num=pl,jj=chinese,in=of]           ->'cats'|'dogs'|'birds'|'animals'|'buffallos'

NNS[cc=both_and,sub=animals,num=pl,jj=red,in=with]         ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=little,in=with]      ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=many,in=with]        ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=nice,in=with]        ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=brown,in=with]       ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=good,in=with]        ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=chinese,in=with]     ->'cats'|'dogs'|'birds'|'buffallos'

NNS[cc=both_and,sub=animals,num=pl,jj=little,in=of]        ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=many,in=of]          ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=brown,in=of]         ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=nice,in=of]          ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=good,in=of]          ->'cats'|'dogs'|'birds'|'buffallos'
NNS[cc=both_and,sub=animals,num=pl,jj=chinese,in=of]       ->'cats'|'dogs'|'birds'|'buffallos'

NNS[det=the,sub=sth,num=pl,jj=many,in=with]      ->'windows'|'points'|'countries'|'thorns'    
NNS[det=the,sub=sth,num=pl,jj=all,in=with]       ->'windows'|'points'|'countries'|'thorns'
NNS[det=the,sub=sth,num=pl,jj=nice,in=with]      ->'windows'|'points'|'countries'|'thorns'
NNS[det=the,sub=sth,num=pl,jj=brown,in=with]     ->'windows'|'points'|'countries'|'thorns'
NNS[det=the,sub=sth,num=pl,jj=good,in=with]      ->'windows'|'points'|'countries'
NNS[det=the,sub=sth,num=pl,jj=chinese,in=with]   ->'windows'|'points'|'countries'|'thorns'
NNS[det=the,sub=sth,num=pl,jj=red,in=with]       ->'windows'
NNS[det=the,sub=sth,num=pl,jj=cheap,in=with]     ->'windows'

NNS[det=the,sub=sth,num=pl,jj=abroad,in=in]      ->'countries'
NNS[det=the,sub=sth,num=pl,jj=many,in=in]        ->'countries'
NNS[det=the,sub=sth,num=pl,jj=all,in=in]         ->'countries'
NNS[det=the,sub=sth,num=pl,jj=good,in=in]        ->'countries'
NNS[det=the,sub=sth,num=pl,jj=chinese,in=in]     ->'countries'

NNS[det=the,sub=human,num=pl,jj=many,in=with]     ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=all,in=with]      ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=nice,in=with]     ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=tall,in=with]     ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=good,in=with]     ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=chinese,in=with]  ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=young,in=with]    ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=little,in=with]   ->'boys'|'models'|'players'|'orphans'

NNS[det=the,sub=human,num=pl,jj=many,in=of]       ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=all,in=of]        ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=nice,in=of]       ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=tall,in=of]       ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=good,in=of]       ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=chinese,in=of]    ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=young,in=of]      ->'boys'|'models'|'players'|'orphans'
NNS[det=the,sub=human,num=pl,jj=little,in=of]     ->'boys'|'models'|'players'|'orphans'


NN[det=the,sub=human,num=sg,jj=hot,in=with]       -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=nice,in=with]      -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=tall,in=with]      -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=good,in=with]      -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=young,in=with]     -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=chinese,in=with]   -> 'girl'|'mother'|'teacher'|'man'

NN[det=the,sub=human,num=sg,jj=hot,in=of]         -> 'girl'|'mother'|'teacher'|'man'                                                     
NN[det=the,sub=human,num=sg,jj=nice,in=of]        -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=tall,in=of]        -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=good,in=of]        -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=young,in=of]       -> 'girl'|'mother'|'teacher'|'man'
NN[det=the,sub=human,num=sg,jj=chinese,in=of]     -> 'girl'|'mother'|'teacher'|'man'
            
NN[det=a,sub=human,num=sg,jj=hot,in=with]         -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=nice,in=with]        -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=tall,in=with]        -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=good,in=with]        -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=young,in=with]       -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=chinese,in=with]     -> 'girl'|'mother'|'teacher'|'man'

NN[det=a,sub=human,num=sg,jj=hot,in=of]           -> 'girl'|'mother'|'teacher'|'man'                                                     
NN[det=a,sub=human,num=sg,jj=nice,in=of]          -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=tall,in=of]          -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=good,in=of]          -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=young,in=of]         -> 'girl'|'mother'|'teacher'|'man'
NN[det=a,sub=human,num=sg,jj=chinese,in=of]       -> 'girl'|'mother'|'teacher'|'man'
                
NN[det=the,sub=sth,num=sg,jj=red,in=with]         -> 'hair'|'pen'|'pencil'|'shirt'|'jacket'|'rose'
NN[det=the,sub=sth,num=sg,jj=brown,in=with]       -> 'hair'|'pen'|'pencil'|'shirt'|'jacket'
NN[det=a,sub=sth,num=sg,jj=brown,in=with]         -> 'hair'|'pen'|'pencil'|'shirt'|'jacket'
NN[det=the,sub=sth,num=sg,jj=blonde,in=with]      -> 'hair'
NN[det=a,sub=sth,num=sg,jj=blonde,in=with]        -> 'hair'
                                                     
                                                     
NN[det=the,sub=sth,num=sg,jj=good,in=of]          -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'apartment'|'class'|'rose'|'coupon'|'trip'
NN[det=a,sub=sth,num=sg,jj=good,in=of]            -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'class'|'rose'|'coupon'|'trip'
NN[det=the,sub=sth,num=sg,jj=nice,in=of]          -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'apartment'|'class'|'rose'|'trip'
NN[det=a,sub=sth,num=sg,jj=nice,in=of]            -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'class'|'rose'|'trip'
NN[det=the,sub=sth,num=sg,jj=chinese,in=of]       -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'apartment'|'class'|'rose'|'trip'
NN[det=a,sub=sth,num=sg,jj=chinese,in=of]         -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'class'|'rose'|'trip'

NN[det=an,sub=sth,num=sg,jj=cheap,in=of]          -> 'apartment'
NN[det=an,sub=sth,num=sg,jj=good,in=of]           -> 'apartment'
NN[det=an,sub=sth,num=sg,jj=nice,in=of]           -> 'apartment'
NN[det=an,sub=sth,num=sg,jj=chinese,in=of]        -> 'apartment'

NN[det=the,sub=sth,num=sg,jj=good,in=with]        -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'money'|'apartment'|'class'|'rose'|'coupon'|'trip'|'trip'
NN[det=a,sub=sth,num=sg,jj=good,in=with]          -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'class'|'rose'|'coupon'|'trip'|'trip'
NN[det=the,sub=sth,num=sg,jj=nice,in=with]        -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'money'|'apartment'|'rose'|'trip'|'trip'
NN[det=a,sub=sth,num=sg,jj=nice,in=with]          -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'class'|'rose'|'trip'|'trip'
NN[det=the,sub=sth,num=sg,jj=chinese,in=with]     -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'money'|'apartment'|'class'|'rose'|'trip'|'trip'
NN[det=a,sub=sth,num=sg,jj=chinese,in=with]       -> 'building'|'match'|'garden'|'hair'|'pen'|'pencil'|'shirt'|'jacket'|'coffee'|'tea'|'weather'|'goverment'|'gambling'|'sky'|'class'|'rose'|'trip'|'trip'
      
NN[det=the,sub=sth,num=sg,jj=cheap,in=with]       -> 'apartment'
NN[det=the,sub=sth,num=sg,jj=red,in=with]         -> 'apartment'
NN[det=the,sub=sth,num=sg,jj=good,in=with]        -> 'apartment'
NN[det=a,sub=sth,num=sg,jj=nice,in=with]          -> 'apartment'
NN[det=the,sub=sth,num=sg,jj=chinese,in=with]     -> 'apartment'

NN[det=the,sub=sth,num=sg,jj=good,in=in]          -> 'building'|'match'|'garden'|'sky'|'class'
NN[det=a,sub=sth,num=sg,jj=good,in=in]            -> 'building'|'match'|'garden'|'sky'|'class'
NN[det=the,sub=sth,num=sg,jj=nice,in=in]          -> 'building'|'match'|'garden'|'sky'|'class'
NN[det=a,sub=sth,num=sg,jj=nice,in=in]            -> 'building'|'match'|'garden'|'sky'|'class'
NN[det=the,sub=sth,num=sg,jj=chinese,in=in]       -> 'building'|'match'|'garden'|'sky'|'class'
NN[det=a,sub=sth,num=sg,jj=chinese,in=in]         -> 'building'|'match'|'garden'|'sky'|'class'
NN[det=a,sub=sth,num=sg,jj=right,in=in]           -> 'side'      

NN[sub=sth,num=sg,jj=popular,in=of]               -> 'baseball'|'football'
NN[sub=sth,num=sg,jj=good,in=of]                  -> 'baseball'|'football'
NN[sub=sth,num=sg,jj=nice,in=of]                  -> 'baseball'|'football'
NN[sub=sth,num=sg,jj=chinese,in=of]               -> 'baseball'|'football'

NNP[sub=sth,num=sg,in=of]   -> 'vietnam'
NNP[sub=sth,num=sg,in=in]   -> 'vietnam'
""")
parser = nltk.parse.FeatureChartParser(grammar)
sentences = ['little cats are bought before the match']
for sent in sentences:
	print(sent)
	words = sent.split()
	for tree in parser.parse(words):
		tree.draw()
