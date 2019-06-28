<template>
  <section class="container">
    <div>
      <h1>8 Queen</h1>
      <table>
      <tbody>
        <tr v-for="(row, index) in tbl" :key="index">
        <td v-for="(data, rowIndex) in row" :key="rowIndex" v-on:click="replaceQueen(index, rowIndex)" :class="data"><p v-if="data=='Placed'"><img src="../assets/chess.png" width="100%" height="100%"></p></td>
        </tr>
      </tbody>
      </table>
      <p v-if="count==8">Complete!</p>
      <div class=button-wrapper>
        <button v-on:click="resetQueen">reset</button>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  data(){
    var count = 0;
    const tbl = Array.from(new Array(8), () => new Array(8).fill(0));
    return {
      tbl,
      count
    };
  },
  methods: {
    replaceQueen: function (index, rowIndex) {
      if(this.tbl[index][rowIndex]) return;
      for (var i=0; i < 8; i++) {
        this.tbl[index][i] = "Placed-line"
        this.tbl[i][rowIndex] = "Placed-line"
        try {
          if ((rowIndex+index-i < 8)&&(rowIndex+index-i > -1)) this.tbl[i][rowIndex+index-i] = "Placed-line"
        } catch(error) {
          console.log(error);
        }
        try {
          if ((index-rowIndex+i < 8)&&(index-rowIndex+i > -1)) this.tbl[index-rowIndex+i][i] = "Placed-line"
        } catch(error) {
          console.log(error);
        }
      }
      this.tbl[index][rowIndex] = "Placed";
      this.count++;
      this.$forceUpdate();
    },
    resetQueen: function () {
      for (var i=0; i<8; i++) {
        for (var j=0; j<8; j++) {
          this.tbl[i][j] = 0;
        }
      }

      this.count = 0;
      this.$forceUpdate();
    }
  },
}
</script>
