#! usr/bin/env python3

lengths = [2, 3, 4 ,6, 7]
pieces = [2, 4, 3, 1, 2]
allPieces = []
for piece in pieces:
    allPieces.extend([lengths.pop()]*piece)


allPieces.sort(reverse=True)
pipes = [12] * len(allPieces)


def firstFull(bins, blocks, reverse=True):
    """
    First fill algorithm used for finding most efficient
    method for combining block elements into bins. Where bins and 
    blocks can be that, or other items such as pipes and pipe lengths

    Returns
    -------
    nBins used, space left
    """
    if reverse:
        blocks.sort(reverse=True)

    maxBin = max(bins)
    for block in range(len(blocks)):
        for binn in range(len(bins)):
            if bins[binn] - blocks[block] >= 0:
                bins[binn] -= blocks[block] 
                blocks[block] = None
                break
    usedBins = [binn for binn in bins if binn < maxBin]
    spaceLeft = sum(usedBins)
    return len(usedBins), spaceLeft

bins, space = firstFull(pipes, allPieces)

print(bins, space)
