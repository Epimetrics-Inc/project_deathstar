import Navsearch from '~/components/navsearch.vue'
import { mount } from 'avoriaz'

describe('navsearch.vue', () => {
  it('Select and deselect all documents', () => {
    const wrapper = mount(Navsearch)

    wrapper.vm.selectAll()
    expect(wrapper.vm.checkedAOs.length).to.equal(wrapper.vm.aoDocuments)
    wrapper.vm.deselectAll()
    expect(wrapper.vm.checkedAOs.length).to.equal(0)
  })

  //select 1 then select all, select 1, then deselect all
})